const BASE='http://127.0.0.1:8766/api/browser/agent/';
let ticking=false;
const executing=new Set();
async function api(path,body,raw=false){
  const {auralyToken}=await chrome.storage.local.get('auralyToken');
  if(!auralyToken) throw Error('Conecte a extensão ao Auraly Studio.');
  const response=await fetch(BASE+path,{method:body!==undefined?'POST':'GET',headers:{'x-auraly-browser-token':auralyToken,'content-type':raw?'application/octet-stream':'application/json'},body:body!==undefined?(raw?body:JSON.stringify(body)):undefined});
  const data=await response.json(); if(!response.ok)throw Error(data.detail || 'Studio indisponível'); return data;
}
async function anchor(job){
  const {auralyToken}=await chrome.storage.local.get('auralyToken');
  const r=await fetch(BASE+`jobs/${job.id}/anchor`,{headers:{'x-auraly-browser-token':auralyToken}});
  if(!r.ok)throw Error('Âncora indisponível ou alterada.');
  const bytes=new Uint8Array(await r.arrayBuffer());
  const hash=[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('');
  if(hash!==job.anchor_sha256)throw Error('A âncora não corresponde à fila.');
  let binary=''; for(let i=0;i<bytes.length;i+=32768)binary+=String.fromCharCode(...bytes.subarray(i,i+32768)); return btoa(binary);
}
async function message(tabId,data){
  const result=await chrome.tabs.sendMessage(tabId,data);
  if(result?.error)throw Error(result.error); return result;
}
async function waitTab(id){
  for(let i=0;i<40;i++){
    const tab=await chrome.tabs.get(id);
    // Newly created tabs may expose no committed URL yet (or about:blank).
    // Wait for the ChatGPT navigation instead of treating that transient state as a departure.
    const url=tab.pendingUrl || tab.url || '';
    if(url && url!=='about:blank' && !url.startsWith('https://chatgpt.com/'))throw Error('A aba saiu do ChatGPT.');
    if(tab.status==='complete' && tab.url?.startsWith('https://chatgpt.com/')){
      try{await message(id,{type:'ping'});return;}catch{}
    }
    await new Promise(r=>setTimeout(r,500));
  }
  throw Error('ChatGPT não ficou pronto. Confira login e a aba.');
}
async function prepare(job){
  const {avatarTabs={}}=await chrome.storage.local.get('avatarTabs');
  const slot=avatarTabs[job.avatar];
  // A user-authorized retry gets a fresh tab; keep the uncertain conversation intact.
  let id=job.retry_of ? null : slot?.id;
  if(id){
    try{
      const t=await chrome.tabs.get(id);
      if(!t.url?.startsWith('https://chatgpt.com/'))throw Error('Aba do avatar navegada para outro site.');
      await message(id,{type:'check-slot',id:slot.job_id});
      await chrome.tabs.update(id,{url:'https://chatgpt.com/'});
    }catch(e){throw Error('A aba do avatar foi fechada ou alterada. Confira antes de retomar.');}
  }else{
    const tab=await chrome.tabs.create({url:'https://chatgpt.com/',active:false}); id=tab.id;
  }
  avatarTabs[job.avatar]={id,job_id:job.id}; await chrome.storage.local.set({avatarTabs});
  await api(`jobs/${job.id}`,{status:'preparing',tab_id:id});
  await waitTab(id);
  const image=await anchor(job);
  await message(id,{type:'prepare',id:job.id,avatar:job.avatar,prompt:job.prompt,anchor:image});
  // Persist before clicking Send. A crash here must never cause an automatic resend.
  await api(`jobs/${job.id}`,{status:'submitting',tab_id:id});
  await message(id,{type:'submit',id:job.id});
  await api(`jobs/${job.id}`,{status:'generating',tab_id:id});
}
function imageURL(value){
  const u=new URL(value);
  if(u.protocol!=='https:' || !(u.hostname==='chatgpt.com'||u.hostname.endsWith('.oaiusercontent.com')))throw Error('Endereço da imagem fora dos domínios de geração.');
  return u.href;
}
async function inspect(job){
  if(!job.tab_id)throw Error('Envio interrompido sem aba registrada. Não reenviado.');
  const tab=await chrome.tabs.get(job.tab_id);
  if(!tab.url?.startsWith('https://chatgpt.com/'))throw Error('A aba foi alterada.');
  const result=await message(job.tab_id,{type:'inspect',id:job.id});
  if(result.kind==='waiting'){
    if(job.status==='submitting' && result.confirmed)await api(`jobs/${job.id}`,{status:'generating',conversation_url:result.url});
    else if(result.url && job.status==='generating' && !job.conversation_url)await api(`jobs/${job.id}`,{status:'generating',conversation_url:result.url});
    if(Date.now()-Date.parse(job.claimed_at)>15*60*1000)throw Error('Geração levou mais de 15 minutos. Confira a conversa; ela não será reenviada.');
    return;
  }
  if(result.kind!=='image')throw Error('Resposta inesperada do ChatGPT.');
  if(job.status==='submitting')await api(`jobs/${job.id}`,{status:'generating',conversation_url:result.url});
  await api(`jobs/${job.id}`,{status:'receiving',conversation_url:result.url});
  let raw;
  if(result.base64)raw=Uint8Array.from(atob(result.base64),c=>c.charCodeAt(0));
  else{
    const response=await fetch(imageURL(result.src),{credentials:'include'});
    if(!response.ok)throw Error('Não foi possível baixar o original da imagem.');
    raw=new Uint8Array(await response.arrayBuffer());
  }
  await api(`jobs/${job.id}/image`,raw,true);
}
async function runJob(job,initial=false){
  if(executing.has(job.id))return;
  executing.add(job.id);
  try{
    if(initial)await prepare(job);
    else if(job.status==='preparing')throw Error('Preparação interrompida. Confira o rascunho antes de retomar.');
    else await inspect(job);
  }catch(e){await api(`jobs/${job.id}`,{status:'attention',error:String(e.message).slice(0,1000)}).catch(()=>{});}
  finally{executing.delete(job.id);}
}
async function tick(){
  if(ticking)return;
  ticking=true;
  try{
    const state=await api('state');
    for(const job of state.jobs.filter(j=>['preparing','submitting','generating','receiving'].includes(j.status)))await runJob(job);
    if(state.running){
      for(let i=0;i<state.concurrency;i++){
        const {job}=await api('claim',{}); if(!job)break;
        await runJob(job,true);
      }
    }
    await chrome.action.setBadgeText({text:state.running?'ON':''});
    return {};
  }catch(e){return {error:e.message};}
  finally{ticking=false;}
}
chrome.runtime.onMessage.addListener((m,sender,reply)=>{
  if(m.type==='wake' && !sender.tab){tick().then(reply);return true;}
});
chrome.alarms.create('auraly',{periodInMinutes:0.5});
chrome.alarms.onAlarm.addListener(a=>{if(a.name==='auraly')tick();});
setInterval(tick,5000);
tick();
