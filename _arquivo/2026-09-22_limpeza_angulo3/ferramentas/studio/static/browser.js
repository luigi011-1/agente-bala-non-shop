const token = document.querySelector('meta[name="studio-token"]').content;
const el = id => document.getElementById(id);
const esc = text => String(text ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let lastJobs = '';
async function api(path, body) {
  const r = await fetch('/api/browser/' + path, {method: body ? 'POST' : 'GET',
    headers: {'content-type':'application/json','x-studio-token':token},
    body: body ? JSON.stringify(body) : undefined});
  const data = await r.json();
  if (!r.ok) throw Error(data.detail || 'Falha no Studio');
  return data;
}
const names = {queued:'Na fila',preparing:'Preparando âncora',submitting:'Enviando',generating:'Gerando no ChatGPT',receiving:'Salvando imagem',done:'Salva · revisão pendente',attention:'Atenção necessária',cancelled:'Tentativa anterior preservada'};
async function refresh() {
  try {
    const state = await api('state');
    const connected = state.connected_at && Date.now() - Date.parse(state.connected_at) < 65000;
    el('connection-status').textContent = `${connected ? 'Chrome conectado' : 'Aguardando conexão da extensão'} · ${state.running ? 'Fila em execução' : 'Novos envios pausados'}`;
    const live = state.jobs.filter(j => j.status !== 'cancelled');
    const signature = JSON.stringify(live.map(j => [j.id, j.status, j.review_status, j.error]));
    if (signature === lastJobs) return;
    lastJobs = signature;
    el('jobs').innerHTML = live.length ? live.map(j => `<article class="attach-row"><div class="browser-job"><b>${esc(j.avatar)} · ${esc(j.frame)}</b><p>${esc(j.review_status === 'approved' && j.status === 'done' ? 'Aprovada' : names[j.status] || j.status)}</p><p class="small muted">${esc(j.error || j.title || '')}</p>${j.conversation_url ? `<a target="_blank" rel="noreferrer" href="${esc(j.conversation_url)}">Abrir conversa</a>` : ''}</div></article>`).join('') : '<p class="muted">Nenhuma imagem em andamento. Prepare a fila dentro de uma produção.</p>';
  } catch (e) { el('notice').textContent = e.message; }
}
async function control(running) {
  try { await api('control', {running, concurrency: 2}); await refresh(); }
  catch (e) { el('notice').textContent = e.message; }
}
el('pause').onclick = () => control(false);
el('resume').onclick = () => control(true);
el('show-connection').onclick = async () => {
  try {
    const d = await api('connection', {});
    el('connection').textContent = `Pasta da extensão:\n${d.extension_dir}\n\nCódigo local (cole apenas na extensão Auraly):\n${d.token}`;
  } catch (e) { el('notice').textContent = e.message; }
};
refresh();
setInterval(refresh, 5000);
