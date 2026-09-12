// Operates only the rendered ChatGPT interface. No private API, cookies or tokens.
let preparing=false;
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
const marker=id=>`AURALY_IMAGE_JOB_${id}`;
const main=()=>document.querySelector('main') || document.querySelector('[role=main]');
function stopReason(){
  const text=(main()?.innerText||'');
  if(/you.ve reached.{0,60}limit|atingiu.{0,60}limite|limite de (criação|geração)|too many requests|try again after|tente novamente (após|às)|something went wrong|ocorreu um erro/i.test(text))return 'O ChatGPT mostrou um limite ou erro. Confira a conversa.';
  if(document.querySelector('iframe[src*="challenges.cloudflare.com"]'))return 'Verificação do navegador pendente.';
}
function editor(){return document.querySelector('#prompt-textarea[contenteditable=true]') || document.querySelector('#prompt-textarea');}
async function until(fn,timeout=45000){const end=Date.now()+timeout;while(Date.now()<end){const reason=stopReason();if(reason)throw Error(reason);const result=fn();if(result)return result;await delay(400);}throw Error('A interface não ficou pronta. Confira a aba.');}
function sendButton(){return document.querySelector('#composer-submit-button') || document.querySelector('[data-testid=send-button]');}
function preflight(){
  const root=main(), e=editor();
  const upload=document.querySelector('#upload-photos')||document.querySelector('input[type=file][accept="image/*"]');
  const busy=root?.querySelector('[data-testid=stop-button]')||root?.querySelector('button[aria-label="Parar streaming"]')||root?.querySelector('button[aria-label="Stop streaming"]');
  const modal=document.querySelector('[role=dialog]')||document.querySelector('[aria-modal=true]')||document.querySelector('iframe[src*="challenges.cloudflare.com"]');
  return {content_script_ready:true,composer_ready:!!e,upload_ready:!!upload,
    draft_empty:!!e&&!e.textContent.trim(),generation_idle:!busy&&!preparing,
    modal_clear:!modal&&!stopReason(),conversation_clean:location.pathname==='/',
    origin:location.origin,pathname:location.pathname};
}
function attachmentSpecs(m){
  const materialized=Array.isArray(m.references)&&m.references.length;
  const refs=materialized?m.references:[{role:'avatar_anchor',data:m.anchor}];
  if(refs.some(r=>!r.role||!r.data))throw Error('Referência obrigatória ausente.');
  if(new Set(refs.map(r=>r.role)).size!==refs.length)throw Error('Referência obrigatória ambígua.');
  return [...refs].sort((a,b)=>a.role.localeCompare(b.role)).map(ref=>({
    ...ref,name:materialized?`auraly-${m.id}-${ref.role}.png`:`auraly-${m.id}.png`}));
}
async function prepare(m){
  if(preparing)throw Error('Esta aba já está preparando uma imagem.');
  preparing=true;
  try{
    if(location.pathname!=='/')throw Error('A conversa precisa estar nova antes do envio.');
    const e=await until(editor);
    if(e.textContent.trim())throw Error('A aba contém um rascunho. Nenhum texto foi substituído.');
    const input=await until(()=>document.querySelector('#upload-photos')||document.querySelector('input[type=file][accept="image/*"]'));
    const refs=attachmentSpecs(m);
    const dt=new DataTransfer();
    const names=[];
    for(const ref of refs){
      const bytes=Uint8Array.from(atob(ref.data),c=>c.charCodeAt(0));
      names.push(ref.name);
      dt.items.add(new File([bytes],ref.name,{type:'image/png'}));
    }
    input.files=dt.files;input.dispatchEvent(new Event('change',{bubbles:true}));
    await until(()=>names.every(name=>(main()?.innerText||'').includes(name) || Array.from(main()?.querySelectorAll('[aria-label],img')||[]).some(i=>((i.getAttribute('aria-label')||'')+(i.alt||'')).includes(name))));
    e.focus();document.execCommand('insertText',false,`${marker(m.id)}\n${m.prompt}`);
    if(!e.textContent.includes(marker(m.id)))throw Error('O prompt não entrou no editor.');
    await until(()=>{const b=sendButton();return b&&!b.disabled;});
    return {ready:true};
  }finally{preparing=false;}
}
async function submit(m){
  verifySubmit(m);
  const b=sendButton();
  b.click();
  await until(()=>!editor()?.textContent.includes(marker(m.id)) && (main()?.innerText||'').includes(marker(m.id)),20000);
  return {submitted:true};
}
function verifySubmit(m){
  const e=editor(),b=sendButton();
  if(!e?.textContent.includes(marker(m.id))||!b||b.disabled)throw Error('Prompt ou anexo não pronto para envio.');
  return {ready:true};
}
async function inspect(m){
  const reason=stopReason();if(reason)throw Error(reason);
  const root=main();if(!root)throw Error('Abra sua sessão do ChatGPT.');
  if(editor()?.textContent.includes(marker(m.id)))throw Error('O envio ficou incerto e o prompt continua no editor. Não reenviado.');
  if(!root.innerText.includes(marker(m.id)))throw Error('Esta conversa não corresponde à imagem da fila.');
  const url=/^\/c\/[\w-]+$/.test(location.pathname)?location.origin+location.pathname:null;
  const busy=root.querySelector('[data-testid=stop-button]') || root.querySelector('button[aria-label="Parar streaming"]') || root.querySelector('button[aria-label="Stop streaming"]');
  const replies=[...root.querySelectorAll('[data-message-author-role="assistant"]')];
  // Current ChatGPT image replies use image-* containers without author-role.
  // Never select arbitrary main img elements: those include the uploaded anchor.
  const generated=[...root.querySelectorAll('img[alt^="Imagem gerada:"],img[alt^="Generated image:"],img[alt^="Image generated:"]')];
  const images=[...new Set([...generated,...replies.flatMap(e=>[...e.querySelectorAll('img')])])].filter(i=>i.complete&&i.naturalWidth>=512&&i.naturalHeight>=512);
  if(busy || !images.length)return {kind:'waiting',url,confirmed:true};
  if(images.length!==1)throw Error('Mais de uma imagem na resposta. Selecione o resultado antes de continuar.');
  const img=images[0];
  if(img.src.startsWith('blob:') || img.src.startsWith('data:')){
    const blob=await (await fetch(img.src)).blob();
    const base64=await new Promise((resolve,reject)=>{const r=new FileReader();r.onload=()=>resolve(r.result.split(',')[1]);r.onerror=reject;r.readAsDataURL(blob);});
    return {kind:'image',base64,url};
  }
  return {kind:'image',src:img.currentSrc||img.src,url};
}
chrome.runtime.onMessage.addListener((m,sender,reply)=>{
  if(sender.id!==chrome.runtime.id)return;
  if(!['ping','preflight','prepare','verify-submit','submit','inspect','check-slot'].includes(m.type))return;
  Promise.resolve().then(()=>{
    if(m.type==='check-slot'){
      if(editor()?.textContent.trim())throw Error('A aba contém um rascunho. Nenhum texto foi substituído.');
      if(!(main()?.innerText||'').includes(marker(m.id)))throw Error('A aba não está mais na conversa vinculada ao avatar.');
      return {ready:true};
    }
    return m.type==='ping'?{ready:true}:m.type==='preflight'?preflight():m.type==='prepare'?prepare(m):m.type==='verify-submit'?verifySubmit(m):m.type==='submit'?submit(m):inspect(m);
  }).then(reply,e=>reply({error:e.message}));
  return true;
});
