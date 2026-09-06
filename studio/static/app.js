const $ = s => document.querySelector(s);
const token = $('meta[name="studio-token"]').content;
const state = {config:null, projects:[], current:null, id:null, selected:[], rendered:null, browser:null};
const names = {uploaded:'Referência recebida',extracted:'Extração concluída',analysis_ready:'Revisar análise',analysis_approved:'Análise aprovada',script_ready:'Revisar roteiro',script_approved:'Roteiro aprovado',hooks_ready:'Escolher ganchos',hooks_selected:'Ganchos escolhidos',imageset_ready:'Avatares e Chrome',upload_error:'Upload incompleto'};
const jobNames = {queued:'Na fila',preparing:'Preparando âncora',submitting:'Enviando',generating:'Gerando no ChatGPT',receiving:'Salvando imagem',done:'Salva · revisão pendente',attention:'Atenção necessária',cancelled:'Tentativa anterior preservada'};
const escape = v => String(v ?? '').replace(/[&<>"']/g, x => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[x]));
const fileURL = (path,id=state.id) => `/api/projects/${id}/files/${path.split('/').map(encodeURIComponent).join('/')}`;
function toast(text){$('#toast').textContent=text;$('#toast').hidden=false;clearTimeout(toast.timer);toast.timer=setTimeout(()=>$('#toast').hidden=true,6500);}
async function api(path,body,method){
  const opts = method || body!==undefined ? {method:method||'POST',headers:{'X-Studio-Token':token}} : {};
  if(body!==undefined){opts.headers['Content-Type']='application/json';opts.body=JSON.stringify(body);}
  const r=await fetch('/api'+path,opts);
  const value=await r.json();
  if(!r.ok)throw new Error(typeof value.detail==='string'?value.detail:JSON.stringify(value.detail));
  return value;
}
async function config(){
  state.config=await api('/config');
  const parts=[];if(state.config.configured)parts.push('OpenAI');if(state.config.gemini_configured)parts.push('Gemini');
  $('#connection-label').textContent=parts.length?parts.join(' + '):'Conectar API';
  $('#connection-dot').classList.toggle('warning',!parts.length);
  $('#text-model').value=state.config.text_model;
  $('#text-provider').value=state.config.text_provider||'auto';
  $('#reasoning-effort').value=state.config.reasoning_effort;
  $('#verification-result').textContent=state.config.verification?.note||'A consulta verifica acesso ao catálogo do modelo de texto; não gera imagens nem comprova saldo ou qualidade.';
}
async function refresh(){
  state.projects=await api('/projects');
  $('#project-count').textContent=state.projects.length;
  $('#projects').innerHTML=state.projects.length?state.projects.map(p=>`<button class="project-item ${p.id===state.id?'active':''}" data-project="${p.id}"><strong>${escape(p.title)}</strong><small>${p.busy?'◌ Em andamento':escape(names[p.status]||p.status)}</small></button>`).join(''):'<p class="small muted">Sua próxima ideia<br>começa aqui.</p>';
  if(state.id){
    const p=await api('/projects/'+state.id);
    state.current=p;
    let browser=null;
    if(p.status==='imageset_ready')browser=await api('/browser/state').catch(()=>null);
    const sig=p.updated+'|'+(browser?JSON.stringify(browser.jobs)+browser.running+browser.connected_at:'');
    if(state.rendered!==sig){state.browser=browser;renderProject(p);renderControls(p);state.rendered=sig;}
  }else renderHome();
}
function renderHome(){
  $('#crumb').textContent='Visão geral';
  $('#content').innerHTML=`<div class="hero"><div class="hero-copy"><div class="eyebrow">AURALY · ÂNGULO 3</div><h1>Da referência<br>ao próximo frame.</h1><p>Analise o vídeo, aprove o roteiro bilíngue, escolha os ganchos e produza as imagens no seu ChatGPT — uma aba por avatar.</p><button class="primary" data-action="new">Criar minha produção ↗</button></div><div class="orbit" aria-hidden="true"></div></div><div class="section-head"><h3>Um processo. Cada detalhe preservado.</h3><span class="small muted">/watch → roteiro → ganchos → ChatGPT no Chrome</span></div><div class="steps-intro">${[['01','Envie a referência','Só o vídeo MP4.'],['02','Roteiro bilíngue','Análise do hook, copy EN + PT, ajuste livre.'],['03','Ganchos visuais','Escolha até 5; valem para todos os avatares.'],['04','Produza no Chrome','Suba as âncoras e gere no seu ChatGPT.']].map(c=>`<article class="intro-card"><div class="number">${c[0]}</div><h3>${c[1]}</h3><p>${c[2]}</p></article>`).join('')}</div><div class="section-head"><h3>Suas produções</h3><span class="small muted">${state.projects.length} no workspace</span></div>${state.projects.length?`<div class="panel"><table><thead><tr><th>PRODUÇÃO</th><th>ETAPA</th><th>AVATARES</th><th></th></tr></thead><tbody>${state.projects.map(p=>`<tr><td>${escape(p.title)}</td><td>${escape(names[p.status]||p.status)}</td><td>${p.avatars||0}</td><td><button data-project="${p.id}">Abrir ↗</button></td></tr>`).join('')}</tbody></table></div>`:'<div class="empty-line">Ainda não há produções. Envie sua primeira referência para começar.</div>'}`;
}
function stageIndex(s){
  if(['uploaded','extracted','analysis_ready','analysis_approved'].includes(s))return 0;
  if(['script_ready','script_approved'].includes(s))return 1;
  if(['hooks_ready','hooks_selected'].includes(s))return 2;
  return 3;
}
function btn(action,label,disabled=false){return `<button class="primary" data-run="${action}" ${disabled?'disabled':''}>${label}</button>`;}
function contextPanel(p){
  const avatar=(p.avatars||[])[0];
  return `<aside class="context-panel"><div class="panel"><div class="eyebrow">REFERÊNCIA</div><div class="preview-pair"><div><video controls preload="metadata" src="${fileURL('source.mp4')}"></video><span class="preview-label">VÍDEO MODELO</span></div>${avatar?`<div><img src="${fileURL(avatar.file)}" alt="Âncora ${escape(avatar.name)}" data-zoom="${fileURL(avatar.file)}"><span class="preview-label">${escape(avatar.name.toUpperCase())}</span></div>`:'<div><div class="asset-placeholder"><b>—</b><span>SEM ÂNCORA</span></div><span class="preview-label">AVATARES</span></div>'}</div><div class="facts"><div class="fact"><span>Duração do modelo</span><b>${Number(p.duration||0).toFixed(1)}s</b></div><div class="fact"><span>Avatares</span><b>${(p.avatars||[]).length}</b></div><div class="fact"><span>Destino</span><b>ChatGPT · Chrome</b></div><div class="fact"><span>Chamadas de texto</span><b>${(p.calls||[]).length}</b></div></div>${p.direction?`<p class="small muted">${escape(p.direction)}</p>`:''}</div><div class="panel"><div class="eyebrow">ATIVIDADE</div>${(p.events||[]).slice(-8).reverse().map(e=>`<div class="event"><time>${new Date(e.time).toLocaleTimeString('pt-BR',{hour:'2-digit',minute:'2-digit'})}</time>${escape(e.message)}</div>`).join('')||'<p class="small muted">Aguardando a primeira etapa.</p>'}<details class="small"><summary>Arquivos de trabalho</summary><p>${escape(state.config.data_dir)}\\${p.id}</p><a href="${fileURL('watch.log')}" target="_blank">Log da extração ↗</a></details></div></aside>`;
}
function analysisView(p){
  let html='<div class="panel"><div class="panel-top"><h3>Análise da referência</h3><span class="pill">/watch</span></div>';
  if(p.status==='uploaded')html+=`<p>Vamos extrair os cortes, todos os frames a cada 0,2s e o áudio para transcrição. Depois, o assistente confere as ações e o herói do hook.</p>${btn('extract','Executar /watch · extração local',p.busy)}`;
  else if(p.status==='extracted')html+=`<p><b>${p.extraction.timeline.length} frames extraídos</b> de ${p.extraction.info.duration}s. A análise ainda não foi feita: o próximo passo percorre todas as grades e amplia o hook e os possíveis reveals.</p><div class="contact-sheets">${p.extraction.overview.timeline.map(s=>`<img src="${fileURL('watch/overview/'+s)}" data-zoom="${fileURL('watch/overview/'+s)}" alt="Grade ${escape(s)}">`).join('')}</div><div class="task-actions">${btn('analyze','Analisar frames com IA',p.busy)}<span class="small muted">Usa OpenAI ou Gemini configurado</span></div>`;
  else if(p.analysis){const a=p.analysis;html+=`<p>${escape(a.summary)}</p><div class="summary-hero"><strong>HERÓI DO HOOK</strong><p>${escape(a.hero)}</p><span class="small muted">Evidências: ${(a.hero_evidence||[]).map(t=>escape(t)+'s').join(' · ')}</span></div><div class="table-wrap"><table><thead><tr><th>TEMPO</th><th>BEAT / VISUAL</th><th>AÇÃO / MUDANÇA</th></tr></thead><tbody>${a.beats.map(b=>`<tr><td class="time">${escape(b.start)}–${escape(b.end)}s</td><td><b>${escape(b.label)}</b><br>${escape(b.visual)}</td><td>${escape(b.change)}<br><span class="muted">${escape(b.props)}</span></td></tr>`).join('')}</tbody></table></div><p class="small muted">${escape(a.continuity)}</p>${a.ambiguity?`<div class="error-note"><b>Um detalhe precisa do seu olhar.</b><p>${(a.questions||[]).map(escape).join('<br>')}</p></div>`:''}${p.status==='analysis_ready'?`<label>Observações ou resposta à dúvida<textarea id="clarification" rows="3" placeholder="Confirme o detalhe do hook, se houver dúvida."></textarea></label><div class="task-actions"><button class="primary" data-action="approve-analysis" ${p.busy?'disabled':''}>Aprovar análise e criar roteiro ↗</button></div>`:''}${p.status==='analysis_approved'?btn('script','Criar roteiro',p.busy):''}<details class="small"><summary>Transcrição original</summary><p>${(p.transcript||[]).map(t=>`[${t.start}s] ${escape(t.text)}`).join('<br>')}</p></details>`;}
  return html+'</div>';
}
function scriptView(p){
  const s=p.script;const editable=p.status==='script_ready';
  return `<div class="panel"><div class="panel-top"><h3>Roteiro bilíngue</h3><span class="pill">${s.takes.reduce((n,t)=>n+t.speech.trim().split(/\s+/).length,0)} palavras</span></div><p class="small muted">${escape(s.notes)}</p>${s.takes.map(t=>`<div class="take"><div class="take-head"><b>${escape(t.id)} · ${escape(t.beat)}</b><span>${t.speech.trim().split(/\s+/).length} palavras · Setup ${escape(t.setup)}</span></div><textarea data-take="${escape(t.id)}" rows="3" ${editable?'':'readonly'}>${escape(t.speech)}</textarea><p class="translation">${escape(t.translation)}</p></div>`).join('')}
  <div class="task-actions">${editable?`<button class="primary" data-action="approve-script" ${p.busy?'disabled':''}>Aprovar roteiro e sugerir ganchos ↗</button>`:p.status==='script_approved'?`<span class="pill">Copy aprovada</span>${btn('hooks','Sugerir ganchos',p.busy)}`:''}</div>
  <details ${p.busy?'open':''}><summary>Ajustar a copy</summary><label>O que mudar (mantém toda a doutrina)<textarea id="copy-note" rows="3" placeholder="Ex.: hook mais direto sobre o instante do pensamento; CTA menos pedidos."></textarea></label><button data-action="adjust-copy" ${p.busy?'disabled':''}>Reescrever roteiro com o ajuste</button></details></div>`;
}
function hooksView(p){
  return `<div class="panel"><div class="panel-top"><h3>Uma copy. Novas aberturas.</h3><span class="pill" id="selected-count">${state.selected.length} / 5 selecionados</span></div><p class="small muted">Escolha até 5 ganchos visuais. Os escolhidos serão gerados para cada avatar; corpo e CTA são compartilhados.</p><div class="hooks">${p.hooks.map(h=>`<label class="hook-card ${state.selected.includes(h.id)?'selected':''}"><input type="checkbox" data-hook="${h.id}" ${state.selected.includes(h.id)?'checked':''} ${p.status!=='hooks_ready'?'disabled':''}><div class="hook-id">${h.id}</div><h3>${escape(h.title)}</h3><p>${escape(h.action)}</p><div class="hook-meta">${escape(h.mechanism)} · ${h.validated?'Referência de banco':'Variação nova'}<br>Prop: ${escape(h.prop)}<br>Congruência: ${escape(h.congruence)}<br>Risco: ${escape(h.risk)}</div></label>`).join('')}</div><div class="task-actions">${p.status==='hooks_ready'?`<button class="primary" data-action="approve-hooks" ${p.busy?'disabled':''}>Montar conjunto de imagens ↗</button>`:p.status==='hooks_selected'?btn('imageset','Montar conjunto de imagens',p.busy):''}</div></div>`;
}
function avatarsView(p){
  const frames=(p.imageset||{}).frames||[];
  const avatars=p.avatars||[];
  const b=state.browser;
  const jobs=b?b.jobs.filter(j=>j.project===p.id):[];
  const connected=b&&b.connected_at&&Date.now()-Date.parse(b.connected_at)<65000;
  const hasJobs=jobs.some(j=>j.status!=='cancelled');
  let html=`<div class="panel"><div class="panel-top"><h3>Avatares desta produção</h3><span class="pill">${frames.length} imagens por avatar</span></div>
  <p class="small muted">Cada arquivo .jpeg é um avatar. A carta SOULMATE já está na mesa da âncora; o prompt põe o mesmo modelo na mão dela. ${escape((p.imageset||{}).notes||'')}</p>
  <div class="gallery">${avatars.map(a=>`<article class="asset-card"><img src="${fileURL(a.file)}" data-zoom="${fileURL(a.file)}" alt="${escape(a.name)}"><div class="asset-info"><h3>${escape(a.name)}</h3>${!hasJobs?`<button data-remove-avatar="${escape(a.id)}">Remover</button>`:''}</div></article>`).join('')||'<p class="muted">Nenhum avatar ainda.</p>'}</div>
  ${!hasJobs?`<label class="dropzone" id="avatar-drop"><span class="upload-icon">↥</span><strong>Arraste os .jpeg dos avatares ou clique</strong><span>JPEG/PNG/WebP · até 20 MB cada · até 8</span><input type="file" id="avatar-files" accept="image/jpeg,image/png,image/webp" multiple></label>`:'<div class="task-actions"><span class="small muted">A fila já foi preparada.</span><button data-action="clear-queue">Limpar fila e trocar avatares</button></div>'}</div>`;

  html+=`<div class="panel"><div class="panel-top"><h3>Produção no Chrome</h3><span class="pill">${connected?'Chrome conectado':'Aguardando extensão'}</span></div>
  <p id="browser-status" class="small muted">${connected?(b.running?'Fila em execução.':'Novos envios pausados.'):'Abra <a href="/browser" target="_blank">Conectar o Chrome</a>, carregue a extensão e cole o código.'}</p>
  <div class="task-actions">
    <label>Cenas por avatar<select id="q-limit"><option value="2">Piloto: primeiras 2</option><option value="">Todas</option></select></label>
    <label>Avatares simultâneos<select id="q-conc"><option>1</option><option selected>2</option><option>3</option><option>4</option></select></label>
    <button data-action="prepare-queue" ${!avatars.length?'disabled':''}>Preparar fila</button>
    <button class="primary" data-action="queue-run" ${!connected||!hasJobs?'disabled':''}>Iniciar / retomar</button>
    <button data-action="queue-pause" ${!hasJobs?'disabled':''}>Pausar novos envios</button>
  </div>
  <p class="small muted">Cada produção vira uma pasta em Downloads / Auraly Studio, com uma subpasta por avatar: imagens + <code>PROMPTS_VIDEO_VEO.txt</code> (prompts de vídeo Veo 3.1 do roteiro final). Pausar preserva as gerações já enviadas. Se uma aba fechar ou um envio ficar incerto, a fila daquele avatar pausa para recuperação; não reenvia sozinha.</p></div>`;

  if(hasJobs){
    html+=`<div class="panel"><div class="panel-top"><h3>Pacotes para o Flow</h3></div>${avatars.map(a=>{
      const js=jobs.filter(j=>j.avatar_id===a.id&&j.status!=='cancelled');
      const ok=js.filter(j=>j.status==='done'&&j.review_status==='approved').length;
      const ready=js.length===frames.length&&ok===frames.length;
      return `<div class="runner-actions"><span><b>${escape(a.name)}</b> · ${ok}/${frames.length} imagens aprovadas</span><button data-export="${escape(a.id)}" ${ready?'':'disabled'}>Baixar pacote</button></div>`;
    }).join('')}</div>`;

    html+=`<div class="panel"><div class="panel-top"><h3>Fila e revisão</h3><span class="pill">${jobs.filter(j=>j.status!=='cancelled').length} imagens</span></div><div id="jobs">${jobs.map(j=>jobCard(j)).join('')}</div></div>`;
  }
  return html;
}
function jobCard(j){
  const label=j.review_status==='approved'&&j.status==='done'?'Aprovada para exportação':(jobNames[j.status]||j.status);
  return `<article class="attach-row"><div class="browser-job"><b>${escape(j.avatar)} · ${escape(j.frame)}</b><p>${escape(label)}</p><p class="small muted">${escape(j.error||j.title||'')}</p>${j.conversation_url?`<a target="_blank" rel="noreferrer" href="${escape(j.conversation_url)}">Abrir conversa</a>`:''}
  ${j.status==='done'?`<a href="/api/browser/jobs/${encodeURIComponent(j.id)}/result" target="_blank" rel="noreferrer"><img class="browser-preview" loading="lazy" src="/api/browser/jobs/${encodeURIComponent(j.id)}/result" alt="${escape(j.avatar)} — ${escape(j.frame)}"></a><p class="small">Confira rosto, mãos, carta, cenário e continuidade antes de aprovar.</p><div class="runner-actions">${j.review_status!=='approved'?`<button data-review="approve" data-job="${escape(j.id)}">Aprovar imagem</button>`:''}<button data-review="retry" data-job="${escape(j.id)}">Gerar nova tentativa</button></div>`:''}
  ${j.status==='attention'?`<div class="runner-actions">${j.tab_id?`<button data-recover="inspect" data-job="${escape(j.id)}">Verificar resultado sem reenviar</button>`:''}<button data-recover="retry" data-job="${escape(j.id)}">Autorizar novo envio</button></div>`:''}
  <details><summary>Prompt exato</summary><pre class="prompt-box">${escape(j.prompt)}</pre></details></div></article>`;
}
function imagesetView(p){return avatarsView(p);}
function renderProject(p){
  $('#crumb').textContent=p.title;
  const idx=stageIndex(p.status);
  state.selected=p.status==='hooks_ready'?state.selected:p.selected||[];
  let work=idx===0?analysisView(p):idx===1?scriptView(p):idx===2?hooksView(p):avatarsView(p);
  if(p.status==='upload_error')work='<div class="panel"><h3>O upload não foi concluído.</h3><p>Crie uma nova produção com um MP4 válido de até 3 minutos.</p><button data-action="new">Nova produção</button></div>';
  $('#content').innerHTML=`<div class="project-heading"><div><div class="eyebrow">ÂNGULO 3</div><h1>${escape(p.title)}</h1><span class="small muted">Referência → roteiro → ganchos → Chrome</span></div><span class="pill">${escape(names[p.status]||p.status)}</span></div><div class="pipeline">${['01 /watch','02 Roteiro','03 Ganchos','04 Chrome'].map((s,i)=>`<div class="pipeline-step ${i===idx?'current':i<idx?'done':''}">${s}</div>`).join('')}</div>${p.busy?`<div class="progress-note">${escape(p.progress||'Iniciando etapa…')}</div>`:''}${p.error?`<div class="error-note">${escape(p.error)}</div>`:''}<div class="work-grid"><div>${work}${idx>0?`<details class="panel"><summary>Consultar análise /watch</summary>${analysisView(p)}</details>`:''}${idx>1?`<details class="panel"><summary>Consultar roteiro aprovado</summary>${scriptView(p)}</details>`:''}${idx>2?`<details class="panel"><summary>Consultar ganchos escolhidos</summary>${hooksView(p)}</details>`:''}</div>${contextPanel(p)}</div>`;
}
async function run(action){await api(`/projects/${state.id}/run/${action}`,{});await refresh();}
async function selectProject(id){state.id=id;state.selected=[];state.rendered=null;history.replaceState(null,'','#'+id);await refresh();}
async function uploadAvatars(files){
  const data=new FormData();
  for(const f of files)data.append('files',f);
  await fetch(`/api/projects/${state.id}/avatars`,{method:'POST',headers:{'X-Studio-Token':token},body:data})
    .then(async r=>{if(!r.ok)throw new Error((await r.json()).detail||'Falha ao subir avatares.');});
  state.rendered=null;await refresh();
}
document.addEventListener('click',async event=>{
  const button=event.target.closest('button,a,img');if(!button)return;
  try{
    if(button.dataset.project){await selectProject(button.dataset.project);return;}
    if(button.dataset.zoom){$('#lightbox-image').src=button.dataset.zoom;$('#lightbox').showModal();return;}
    if(button.dataset.run){button.disabled=true;await run(button.dataset.run);return;}
    if(button.dataset.removeAvatar){button.disabled=true;await api(`/projects/${state.id}/avatars/${button.dataset.removeAvatar}`,undefined,'DELETE');state.rendered=null;await refresh();return;}
    if(button.dataset.review){button.disabled=true;const retry=button.dataset.review==='retry';if(retry&&!confirm('Criar nova tentativa? Pode consumir sua cota do ChatGPT. O resultado anterior é preservado.'))return;await api(`/browser/jobs/${encodeURIComponent(button.dataset.job)}/review`,{decision:button.dataset.review});state.rendered=null;await refresh();return;}
    if(button.dataset.recover){button.disabled=true;await api(`/browser/jobs/${encodeURIComponent(button.dataset.job)}/recover`,{action:button.dataset.recover});state.rendered=null;await refresh();return;}
    if(button.dataset.export){button.disabled=true;const r=await fetch(`/api/browser/projects/${state.id}/avatars/${button.dataset.export}/export`,{method:'POST',headers:{'X-Studio-Token':token}});if(!r.ok)throw new Error((await r.json()).detail||'Não foi possível exportar.');const url=URL.createObjectURL(await r.blob());const a=document.createElement('a');a.href=url;a.download=`auraly-chrome.zip`;a.click();setTimeout(()=>URL.revokeObjectURL(url),60000);toast('Pacote exportado.');button.disabled=false;return;}
    if(button.dataset.action==='verify-connection'){button.disabled=true;const result=await api('/config/verify',{});$('#verification-result').textContent=result.note;toast(result.note);return;}
    if(button.dataset.action==='pause-production'){await api(`/projects/${state.id}/pause`,{});await refresh();return;}
    if(button.dataset.action==='save-limits'){await api(`/projects/${state.id}/limits`,{text:Number($('#limit-text').value)});await refresh();toast('Limite atualizado.');return;}
    if(button.dataset.action==='adjust-copy'){button.disabled=true;await api(`/projects/${state.id}/adjust-copy`,{copy_note:$('#copy-note')?.value||''});await refresh();return;}
    if(button.dataset.action==='prepare-queue'){button.disabled=true;const v=$('#q-limit').value;await api(`/projects/${state.id}/queue`,{ids:[state.id],limit:v?Number(v):null});state.rendered=null;await refresh();toast('Fila preparada.');return;}
    if(button.dataset.action==='clear-queue'){if(!confirm('Limpar a fila desta produção? As imagens já salvas em Downloads permanecem.'))return;button.disabled=true;await api(`/projects/${state.id}/queue/clear`,{});state.rendered=null;await refresh();toast('Fila limpa.');return;}
    if(button.dataset.action==='queue-run'){button.disabled=true;await api('/browser/control',{running:true,concurrency:Number($('#q-conc').value)});state.rendered=null;await refresh();return;}
    if(button.dataset.action==='queue-pause'){button.disabled=true;await api('/browser/control',{running:false,concurrency:Number($('#q-conc').value)});state.rendered=null;await refresh();return;}
    switch(button.dataset.action){
      case'new':$('#new-dialog').showModal();break;
      case'close-new':$('#new-dialog').close();break;
      case'settings':$('#settings-dialog').showModal();break;
      case'close-settings':$('#settings-dialog').close();break;
      case'close-lightbox':$('#lightbox').close();break;
      case'disconnect':await api('/config',{api_key:'',gemini_key:'',text_model:$('#text-model').value,reasoning_effort:$('#reasoning-effort').value});await config();toast('Conexões removidas e credenciais salvas esvaziadas.');break;
      case'approve-analysis':button.disabled=true;await api(`/projects/${state.id}/approve/analysis`,{clarification:$('#clarification')?.value||''});await refresh();await run('script');break;
      case'approve-script':{const script=structuredClone(state.current.script);document.querySelectorAll('textarea[data-take]').forEach(el=>{script.takes.find(t=>t.id===el.dataset.take).speech=el.value.trim();});button.disabled=true;await api(`/projects/${state.id}/approve/script`,{script});await refresh();await run('hooks');break;}
      case'approve-hooks':button.disabled=true;await api(`/projects/${state.id}/approve/hooks`,{selected:state.selected});await refresh();await run('imageset');break;
    }
  }catch(error){if(button.dataset.action==='verify-connection')$('#verification-result').textContent=error.message;toast(error.message);}
  finally{button.disabled=false;}
});
document.addEventListener('change',e=>{
  if(e.target.dataset.hook){
    const id=e.target.dataset.hook;
    if(e.target.checked&&state.selected.length>=5){e.target.checked=false;toast('Selecione até cinco ganchos.');return;}
    state.selected=e.target.checked?[...state.selected,id]:state.selected.filter(h=>h!==id);
    e.target.closest('.hook-card').classList.toggle('selected',e.target.checked);
    $('#selected-count').textContent=state.selected.length+' / 5 selecionados';
  }
  if(e.target.id==='avatar-files'&&e.target.files.length){uploadAvatars([...e.target.files]).catch(err=>toast(err.message));}
});
document.addEventListener('dragover',e=>{if(e.target.closest('#avatar-drop')){e.preventDefault();e.target.closest('#avatar-drop').classList.add('over');}});
document.addEventListener('drop',e=>{const d=e.target.closest('#avatar-drop');if(!d)return;e.preventDefault();d.classList.remove('over');if(e.dataTransfer.files.length)uploadAvatars([...e.dataTransfer.files]).catch(err=>toast(err.message));});
$('#video-file').addEventListener('change',e=>$('#file-label').textContent=e.target.files[0]?.name||'Arraste seu vídeo ou clique para escolher');
const drop=$('#dropzone');drop.addEventListener('dragover',e=>{e.preventDefault();drop.classList.add('over');});drop.addEventListener('dragleave',()=>drop.classList.remove('over'));drop.addEventListener('drop',e=>{e.preventDefault();drop.classList.remove('over');if(e.dataTransfer.files.length){$('#video-file').files=e.dataTransfer.files;$('#file-label').textContent=e.dataTransfer.files[0].name;}});
$('#upload-form').addEventListener('submit',e=>{
  e.preventDefault();const data=new FormData(e.target);const xhr=new XMLHttpRequest();
  xhr.open('POST','/api/projects');xhr.setRequestHeader('X-Studio-Token',token);
  $('#upload-button').disabled=true;$('#upload-progress').hidden=false;$('#upload-status').textContent='Enviando referência…';
  xhr.upload.onprogress=e=>{if(e.lengthComputable)$('#upload-progress').value=e.loaded/e.total*100;};
  xhr.onload=async()=>{try{const p=JSON.parse(xhr.responseText);if(xhr.status>=400)throw Error(typeof p.detail==='string'?p.detail:'Falha no upload.');$('#new-dialog').close();$('#upload-form').reset();$('#file-label').textContent='Arraste seu vídeo ou clique para escolher';await selectProject(p.id);toast('Produção criada. Pronta para /watch.');}catch(error){toast(error.message);}finally{$('#upload-button').disabled=false;$('#upload-progress').hidden=true;$('#upload-status').textContent='Ângulo 3 · Auraly';}};
  xhr.onerror=()=>{$('#upload-button').disabled=false;toast('Conexão local interrompida durante o upload.');};
  xhr.send(data);
});
$('#settings-form').addEventListener('submit',async e=>{
  e.preventDefault();
  try{
    const body={text_provider:$('#text-provider').value,text_model:$('#text-model').value,reasoning_effort:$('#reasoning-effort').value};
    if($('#api-key').value.trim())body.api_key=$('#api-key').value.trim();
    if($('#gemini-key').value.trim())body.gemini_key=$('#gemini-key').value.trim();
    await api('/config',body);
    $('#api-key').value='';$('#gemini-key').value='';
    await config();
    $('#verification-result').textContent='Configuração salva.';
  }catch(error){$('#verification-result').textContent=error.message;}
});
function renderControls(p){
  const panel=document.querySelector('.context-panel');if(!panel)return;
  const controls=document.createElement('div');controls.className='panel';
  controls.innerHTML=`<div class="eyebrow">CONTROLE</div><p class="small">${escape(state.config.text_model)} · raciocínio ${escape(state.config.reasoning_effort)} (OpenAI). Fallback: ${escape(state.config.gemini_model)}.</p><p class="small muted">Limite cumulativo de chamadas de texto do projeto. Conta chamadas enviadas, inclusive falhas.</p><label>Chamadas de texto (${(p.calls||[]).length} usadas)<input id="limit-text" type="number" min="1" max="1000" value="${p.call_limits?.text||200}" ${p.busy?'disabled':''}></label><button data-action="save-limits" ${p.busy?'disabled':''}>Salvar limite</button>${p.busy?'<button data-action="pause-production">Pausar antes da próxima chamada</button>':''}${p.pause_requested?'<p class="small">Pausa solicitada. Chamadas em andamento podem concluir. Retome pela etapa atual.</p>':''}`;
  panel.prepend(controls);
}
async function init(){try{await config();const id=location.hash.slice(1);if(/^[a-f0-9]{32}$/.test(id))state.id=id;await refresh();}catch(error){toast(error.message);}setInterval(()=>refresh().catch(()=>{}),2500);}
init();
