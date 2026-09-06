const token = document.querySelector('meta[name="studio-token"]').content;
const el = id => document.getElementById(id);
const esc = text => String(text ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let lastJobs = '';
async function api(path, body) {
  const r = await fetch('/api/browser/' + path, {method: body ? 'POST' : 'GET', headers: {'content-type':'application/json','x-studio-token':token}, body:body ? JSON.stringify(body) : undefined});
  const data = await r.json(); if (!r.ok) throw Error(data.detail || 'Falha no Studio'); return data;
}
async function refresh() {
  try {
    const state = await api('state');
    const connected = state.connected_at && Date.now() - Date.parse(state.connected_at) < 65000;
    el('connection-status').textContent = `${connected ? 'Chrome conectado' : 'Aguardando conexão da extensão'} · ${state.running ? 'Fila em execução' : 'Novos envios pausados'}`;
    el('start').disabled = !connected || !state.jobs.length;
    const names = {queued:'Na fila',preparing:'Preparando âncora',submitting:'Enviando',generating:'Gerando no ChatGPT',receiving:'Salvando imagem',done:'Salva · revisão pendente',attention:'Atenção necessária',cancelled:'Tentativa anterior preservada'};
    const signature = JSON.stringify(state.jobs);
    if (signature !== lastJobs) {
      lastJobs = signature;
      el('jobs').innerHTML = state.jobs.length ? state.jobs.map(j => `<article class="attach-row"><div class="browser-job"><b>${esc(j.avatar)} · ${esc(j.frame)}</b><p>${esc(j.review_status === 'approved' && j.status === 'done' ? 'Aprovada para exportação' : names[j.status] || j.status)}</p><p class="small muted">${esc(j.error || j.file || j.title)}</p>${j.conversation_url ? `<a target="_blank" rel="noreferrer" href="${esc(j.conversation_url)}">Abrir conversa</a>` : ''}
      ${j.status === 'done' ? `<a href="/api/browser/jobs/${encodeURIComponent(j.id)}/result" target="_blank" rel="noreferrer"><img class="browser-preview" loading="lazy" src="/api/browser/jobs/${encodeURIComponent(j.id)}/result" alt="${esc(j.avatar)} — ${esc(j.frame)}. Abrir imagem completa."></a><p class="small">Confira rosto, mãos, carta, cenário e continuidade antes de aprovar.</p><div class="runner-actions">${j.review_status !== 'approved' ? `<button data-review="approve" data-job="${esc(j.id)}">Aprovar imagem</button>` : ''}<button class="secondary" data-review="retry" data-job="${esc(j.id)}">Gerar nova tentativa</button></div>` : ''}
      ${j.status === 'attention' ? `<div class="runner-actions">${j.tab_id ? `<button data-recover="inspect" data-job="${esc(j.id)}">Verificar resultado sem reenviar</button>` : ''}<button class="secondary" data-recover="retry" data-job="${esc(j.id)}">Autorizar novo envio</button></div>` : ''}
      <details><summary>Prompt exato e âncora</summary><p class="small">SHA-256 da âncora: ${esc(j.anchor_sha256)}</p><pre class="prompt-box">${esc(j.prompt)}</pre></details></div></article>`).join('') : '<p class="muted">Selecione as produções e prepare a fila.</p>';
      const projects = [...new Set(state.jobs.map(j=>j.project))];
      el('exports').innerHTML = projects.map(pid=> {const js=state.jobs.filter(j=>j.project===pid && j.status!=='cancelled');const approved=js.filter(j=>j.status==='done' && j.review_status==='approved').length;return `<div class="runner-actions"><span><b>${esc(js[0]?.avatar || 'Produção')}</b> · ${esc(pid.slice(0,8))} · ${approved}/${js.length} imagens da fila aprovadas</span><button data-export="${esc(pid)}" ${!js.length || approved!==js.length ? 'disabled' : ''}>Baixar pacote completo</button></div>`;}).join('') || '<p class="muted">Os pacotes aparecem após preparar a fila.</p>';
    }
  } catch(e) { el('notice').textContent = e.message; }
}
async function action(fn) { try { await fn(); await refresh(); } catch(e) { el('notice').textContent = e.message; } }
el('enqueue').onclick = () => action(async () => { const ids = [...document.querySelectorAll('#project-list input:checked')].map(e=>e.value); if(!ids.length) throw Error('Escolha pelo menos uma produção.'); await api('queue',{ids,limit:el('limit').value ? Number(el('limit').value) : null}); el('notice').textContent='Fila preparada. Confira os prompts abaixo e inicie.'; });
el('start').onclick = () => action(()=>api('control',{running:true,concurrency:Number(el('concurrency').value)}));
el('pause').onclick = () => action(()=>api('control',{running:false,concurrency:Number(el('concurrency').value)}));
el('show-connection').onclick = () => action(async()=> {const d=await api('connection',{}); el('connection').textContent=`Pasta da extensão:\n${d.extension_dir}\n\nCódigo local (cole apenas na extensão Auraly):\n${d.token}`;});
fetch('/api/projects').then(r=>r.json()).then(ps=> {el('project-list').innerHTML=ps.filter(p=>['plan_ready','generating','complete'].includes(p.status)).map(p=>`<label class="project-pick"><input type="checkbox" value="${esc(p.id)}"><span><b>${esc(p.avatar)}</b><span class="small muted">${esc(p.title)}</span></span></label>`).join('');}).catch(e=>el('notice').textContent=e.message);
refresh(); setInterval(refresh,5000);

el('jobs').addEventListener('click', event => {
  const button = event.target.closest('button[data-job]');
  if (!button) return;
  const jid = encodeURIComponent(button.dataset.job);
  const retry = (button.dataset.review || button.dataset.recover) === 'retry';
  if (retry && !confirm('Criar uma nova tentativa? Isso pode consumir sua cota do ChatGPT. O resultado anterior será preservado.')) return;
  action(async()=>{
    button.disabled = true;
    try {
      if (button.dataset.review) await api(`jobs/${jid}/review`, {decision:button.dataset.review});
      else await api(`jobs/${jid}/recover`, {action:button.dataset.recover});
      lastJobs = '';
      button.blur();
      el('notice').textContent = retry ? 'Nova tentativa na fila. Use Iniciar / retomar quando estiver pronto.' : 'Revisão registrada.';
    } finally { button.disabled = false; }
  });
});
el('exports').addEventListener('click', event => {
  const button = event.target.closest('button[data-export]');
  if (!button) return;
  action(async()=>{
    button.disabled = true;
    try {
      const r = await fetch(`/api/browser/projects/${encodeURIComponent(button.dataset.export)}/export`, {method:'POST',headers:{'x-studio-token':token}});
      if (!r.ok) throw Error((await r.json()).detail || 'Não foi possível exportar.');
      const url = URL.createObjectURL(await r.blob());
      const a = document.createElement('a');a.href=url;a.download=`auraly-${button.dataset.export.slice(0,8)}-flow.zip`;a.click();
      setTimeout(()=>URL.revokeObjectURL(url),60000);
      el('notice').textContent='Pacote exportado com imagens aprovadas e prompts para o Flow.';
    } finally { button.disabled = false; }
  });
});
