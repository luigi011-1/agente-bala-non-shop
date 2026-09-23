const BASE='http://127.0.0.1:8765/api/browser/agent/';
let ticking=false;
const executing=new Set();
// Phase B: background job tracking so tick() fires jobs without blocking itself
const runningJobs=new Map(); // job.id -> Promise
// Shared reference cache: sha256 -> base64 (settled). Immutable once verified.
// K01-K04 share the same anchor and REF-CARTA; one fetch serves all four.
const refCache=new Map();
// In-flight deduplication: sha256 -> Promise<base64>.
// When 4 concurrent materializedReferences calls race before the first cache settles,
// the second through fourth await the same Promise instead of firing duplicate fetches.
const refInflight=new Map();
const extensionSessionId=crypto.randomUUID();
// Declared capabilities of this service worker build.
// The backend compares this against its required set on every heartbeat.
// If this list is missing a required capability, heartbeat() returns
// {extension_reload_required: true} and tick() bails out immediately.
const AGENT_PROTOCOL_VERSION='2.0.0';
const AGENT_CAPABILITIES=[
  'canonical_materialized_jobs',
  'multiple_references',
  'preflight_handshake',
  'preflight_polling',
  'batch_preflight',
  'dedicated_tab_creation',
  'parallel_tick',
  'ref_cache',
];
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
async function materializedReferences(job){
  if(job.job_kind!=='canonical_materialized')throw Error('Contrato materializado inválido.');
  if(job.execution_ready!==true)throw Error('Job materializado não está habilitado para execução.');
  const refs=Array.isArray(job.references)?job.references:[];
  const roles=new Set(refs.map(r=>r.role));
  if(['K01_hook_card_pull_camera','K02_hook_salt_circle_closing','K03_hook_honey_over_card','K04_body_reading_t2_t4'].includes(job.asset_id)
      && !(roles.has('avatar_anchor')&&roles.has('shared_card_reference')))throw Error('Referência obrigatória ausente.');
  if(roles.size!==refs.length)throw Error('Referência obrigatória ambígua.');
  const {auralyToken}=await chrome.storage.local.get('auralyToken');
  return Promise.all([...refs].sort((a,b)=>a.role.localeCompare(b.role)).map(async ref=>{
    // Settled cache hit: verified bytes already in hand
    if(refCache.has(ref.sha256))return {role:ref.role,sha256:ref.sha256,data:refCache.get(ref.sha256)};
    // In-flight deduplication: if a parallel call is already fetching the same sha256, await it
    if(refInflight.has(ref.sha256)){
      const data=await refInflight.get(ref.sha256);
      return {role:ref.role,sha256:ref.sha256,data};
    }
    // New fetch: register the Promise before awaiting so concurrent calls join it
    const fetchPromise=(async()=>{
      const r=await fetch(BASE+`jobs/${job.id}/references/${encodeURIComponent(ref.role)}`,{headers:{'x-auraly-browser-token':auralyToken}});
      if(!r.ok)throw Error(`Referência ${ref.role} indisponível ou alterada.`);
      const bytes=new Uint8Array(await r.arrayBuffer());
      const hash=[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(x=>x.toString(16).padStart(2,'0')).join('');
      if(hash!==ref.sha256)throw Error(`A referência ${ref.role} não corresponde à fila.`);
      let binary='';for(let i=0;i<bytes.length;i+=32768)binary+=String.fromCharCode(...bytes.subarray(i,i+32768));
      return btoa(binary);
    })();
    refInflight.set(ref.sha256,fetchPromise);
    let data;
    try{data=await fetchPromise;}finally{refInflight.delete(ref.sha256);}
    refCache.set(ref.sha256,data);
    return {role:ref.role,sha256:ref.sha256,data};
  }));
}
async function message(tabId,data){
  const result=await chrome.tabs.sendMessage(tabId,data);
  if(result?.error)throw Error(result.error); return result;
}
function nonce(){return crypto.randomUUID();}
function cleanReport(job,tab,content,requestNonce){
  return {job_id:job.id,canonical_asset_fingerprint:job.canonical_asset_fingerprint,
    tab_id:tab.id,window_id:tab.windowId,url:tab.url,extension_session_id:extensionSessionId,
    nonce:requestNonce,...content};
}
// createNew=true: auto-create a tab instead of searching for one.
// Used by handlePreflightRequest (batch path) so each job in a concurrent preflight
// round gets its own dedicated tab without colliding with siblings.
async function exactPreflight(job,requestedTabId,createNew=false){
  if(job.job_kind!=='canonical_materialized'||job.execution_ready!==false)throw Error('Preflight aceito somente para job materializado desativado.');
  let tab;
  if(requestedTabId!==undefined&&requestedTabId!==null){
    tab=await chrome.tabs.get(requestedTabId);
  }else if(createNew){
    tab=await chrome.tabs.create({url:'https://chatgpt.com/',active:false});
    await waitTab(tab.id);
  }else{
    const candidates=(await chrome.tabs.query({url:'https://chatgpt.com/'})).filter(t=>t.url==='https://chatgpt.com/'&&t.status==='complete');
    if(candidates.length!==1)throw Error(candidates.length?'Há mais de uma aba ChatGPT elegível; escolha a aba explicitamente.':'Não há uma aba ChatGPT nova e elegível.');
    tab=candidates[0];
  }
  if(tab.status!=='complete'||tab.url!=='https://chatgpt.com/')throw Error('A aba indicada não é uma conversa nova válida do ChatGPT.');
  const check=await message(tab.id,{type:'preflight'});
  const report=cleanReport(job,tab,check,nonce());
  if(!['content_script_ready','composer_ready','upload_ready','draft_empty','generation_idle','modal_clear','conversation_clean'].every(k=>report[k]===true))throw Error('A aba indicada não está operacionalmente limpa.');
  return api('preflight',report);
}
async function handlePreflightRequest(request,job){
  // Readiness-only path: never claims, changes execution_ready, downloads references or touches composer text.
  // Marks 'checking' immediately so concurrent tick()s don't re-process the same request.
  try{
    await api('preflight-requests/checking',{request_id:request.request_id,job_id:request.job_id,
      canonical_asset_fingerprint:request.canonical_asset_fingerprint,extension_session_id:extensionSessionId});
    if(!job||job.job_kind!=='canonical_materialized'||job.execution_ready!==false
       ||job.canonical_asset_fingerprint!==request.canonical_asset_fingerprint)throw Error('Job ou fingerprint não é mais elegível para preflight.');
    // When no specific tab is requested, auto-create so concurrent batch preflights
    // each get their own tab without interfering with siblings.
    await exactPreflight(job,request.requested_tab_id,request.requested_tab_id==null);
  }catch(e){
    await api('preflight-requests/failed',{request_id:request.request_id,extension_session_id:extensionSessionId,
      error:String(e.message).slice(0,1000)}).catch(()=>{});
  }
}
async function activateWithRevalidation(job,preflight){
  // Intentionally explicit: no tick/claim path invokes this. It never searches another tab.
  const tab=await chrome.tabs.get(preflight.tab_id);
  if(tab.windowId!==preflight.window_id||tab.url!==preflight.url)throw Error('A aba validada mudou; preflight inválido.');
  const check=await message(tab.id,{type:'preflight'});
  const report=cleanReport(job,tab,check,nonce());
  return api(`jobs/${job.id}/activate`,{canonical_asset_fingerprint:job.canonical_asset_fingerprint,
    preflight_id:preflight.preflight_id,revalidation:report});
}
// Auto-activate all valid preflights found in state, concurrently.
// This closes the loop: preflight registered -> activate in same tick cycle, no manual step.
// Preflights whose linked preflight_request carries allow_activation===false are skipped:
// they belong to benchmark/preflight_only batches and must never be submitted.
async function autoActivatePreflights(state){
  const validPreflights=(state.preflights||[]).filter(p=>p.status==='valid');
  if(!validPreflights.length)return;
  await Promise.allSettled(validPreflights.map(async preflight=>{
    const request=(state.preflight_requests||[]).find(r=>r.preflight_id===preflight.preflight_id);
    if(request&&request.allow_activation===false)return;
    const job=state.jobs.find(j=>j.id===preflight.job_id&&j.job_kind==='canonical_materialized'&&!j.execution_ready);
    if(!job)return;
    try{await activateWithRevalidation(job,preflight);}catch{}
  }));
}
async function assertAuthorizedTarget(job){
  if(job.job_kind!=='canonical_materialized')return;
  const target=job.authorized_target;
  if(!target||job.activation_preflight_id!==target.preflight_id||job.authorized_extension_session_id!==extensionSessionId
      ||target.extension_session_id!==extensionSessionId)throw Error('A sessão não corresponde ao alvo autorizado; novo preflight necessário.');
  const tab=await chrome.tabs.get(target.tab_id);
  if(tab.id!==job.tab_id||tab.windowId!==target.window_id||tab.url!==target.url||tab.url!==job.preflight_url)
    throw Error('A aba não corresponde ao alvo autorizado; novo preflight necessário.');
  const check=await message(tab.id,{type:'preflight'});
  if(!['content_script_ready','composer_ready','upload_ready','draft_empty','generation_idle','modal_clear','conversation_clean'].every(k=>check[k]===true))
    throw Error('A aba autorizada deixou de estar limpa; novo preflight necessário.');
  return tab;
}
async function waitTab(id){
  for(let i=0;i<40;i++){
    const tab=await chrome.tabs.get(id);
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
  const t0=Date.now();
  if(job.job_kind==='canonical_materialized'&&job.execution_ready!==true)throw Error('Job materializado não está habilitado para execução.');
  const authorizedTab=job.job_kind==='canonical_materialized'?await assertAuthorizedTarget(job):null;
  // Resolve references before touching any tab; cache means K01-K04 share one fetch per file
  const refs=job.job_kind==='canonical_materialized'?await materializedReferences(job):null;
  const t1=Date.now();
  const {avatarTabs={}}=await chrome.storage.local.get('avatarTabs');
  const key=job.avatar_key||job.avatar;
  const slot=avatarTabs[key];
  let id=job.job_kind==='canonical_materialized'?authorizedTab.id:(job.retry_of ? null : slot?.id);
  if(id){
    try{
      const t=await chrome.tabs.get(id);
      if(job.job_kind==='canonical_materialized'&&(t.windowId!==job.window_id||t.url!==job.preflight_url))throw Error('Aba materializada divergiu do alvo autorizado.');
      if(!t.url?.startsWith('https://chatgpt.com/'))throw Error('Aba do avatar navegada para outro site.');
      if(job.job_kind!=='canonical_materialized'){
        await message(id,{type:'check-slot',id:slot.job_id});
        await chrome.tabs.update(id,{url:'https://chatgpt.com/'});
      }
    }catch(e){throw Error('A aba do avatar foi fechada ou alterada. Confira antes de retomar.');}
  }else{
    const tab=await chrome.tabs.create({url:'https://chatgpt.com/',active:false}); id=tab.id;
  }
  avatarTabs[key]={id,job_id:job.id}; await chrome.storage.local.set({avatarTabs});
  await api(`jobs/${job.id}`,{status:'preparing',tab_id:id});
  await waitTab(id);
  const t2=Date.now();
  const legacyAnchor=job.job_kind==='canonical_materialized'?null:await anchor(job);
  if(job.job_kind==='canonical_materialized')await assertAuthorizedTarget(job);
  await message(id,{type:'prepare',id:job.id,avatar:job.avatar,prompt:job.prompt,
                    anchor:legacyAnchor,references:refs});
  const t3=Date.now();
  await message(id,{type:'verify-submit',id:job.id});
  await api(`jobs/${job.id}`,{status:'submitting',tab_id:id});
  await message(id,{type:'submit',id:job.id});
  const t4=Date.now();
  await api(`jobs/${job.id}`,{status:'generating',tab_id:id});
  console.log(`[auraly] ${job.frame||job.asset_id} refs:${t1-t0}ms tab:${t2-t1}ms upload+fill:${t3-t2}ms submit:${t4-t3}ms total:${t4-t0}ms`);
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
  if(job.job_kind==='canonical_materialized'&&job.execution_ready!==true)return;
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
    const state=await api('state',{extension_session_id:extensionSessionId,
      agent_protocol_version:AGENT_PROTOCOL_VERSION,agent_capabilities:AGENT_CAPABILITIES});
    if(state.extension_reload_required)throw Error('Extensão desatualizada; recarregue em chrome://extensions antes de continuar.');

    // 1. Preflight requests: fire all concurrently, don't await.
    //    Each handler marks itself 'checking' immediately, preventing re-processing by the next tick.
    const pendingPreflights=(state.preflight_requests||[]).filter(r=>r.status==='requested');
    if(pendingPreflights.length){
      await Promise.allSettled(pendingPreflights.map(r=>
        handlePreflightRequest(r,state.jobs.find(j=>j.id===r.job_id))
      ));
    }

    // 2. Auto-activate all valid preflights concurrently.
    //    Closes the preflight -> execution_ready=true loop without manual UI step.
    await autoActivatePreflights(state);

    // 3. Resume active jobs that are not already running: fire in background.
    for(const job of state.jobs.filter(j=>
        ['preparing','submitting','generating','receiving'].includes(j.status)
        &&(j.job_kind!=='canonical_materialized'||j.execution_ready===true))){
      if(!runningJobs.has(job.id)){
        const p=runJob(job).finally(()=>runningJobs.delete(job.id));
        runningJobs.set(job.id,p);
      }
    }

    // 4. Claim new jobs up to available concurrency slots; all claims in parallel.
    if(state.running){
      const slots=Math.max(0,state.concurrency-runningJobs.size);
      if(slots>0){
        const claims=await Promise.all(Array.from({length:slots},()=>api('claim',{})));
        for(const {job} of claims){
          if(job&&!runningJobs.has(job.id)){
            const p=runJob(job,true).finally(()=>runningJobs.delete(job.id));
            runningJobs.set(job.id,p);
          }
        }
      }
    }

    await chrome.action.setBadgeText({text:state.running?'ON':''});
    return {};
  }catch(e){return {error:e.message};}
  finally{ticking=false;}
}
chrome.runtime.onMessage.addListener((m,sender,reply)=>{
  if(m.type==='wake' && !sender.tab){tick().then(reply);return true;}
  if(m.type==='preflight' && !sender.tab){exactPreflight(m.job,m.tab_id).then(reply,e=>reply({error:e.message}));return true;}
  if(m.type==='activate-preflight' && !sender.tab){activateWithRevalidation(m.job,m.preflight).then(reply,e=>reply({error:e.message}));return true;}
});
chrome.alarms.create('auraly',{periodInMinutes:0.5});
chrome.alarms.onAlarm.addListener(a=>{if(a.name==='auraly')tick();});
setInterval(tick,5000);
tick();
