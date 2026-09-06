const TOKEN = document.querySelector('meta[name="studio-token"]').content;
const state = { steps: [], index: 0, watching: false };

async function api(path, body) {
  const options = { method: body ? 'POST' : 'GET', headers: { 'x-studio-token': TOKEN } };
  if (body) { options.headers['Content-Type'] = 'application/json'; options.body = JSON.stringify(body); }
  const response = await fetch(path, options);
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data.detail || 'Falha na requisição.');
  return data;
}

const el = id => document.getElementById(id);

async function loadProjects() {
  const projects = await api('/api/projects');
  const ready = projects.filter(p => ['plan_ready', 'generating', 'complete'].includes(p.status));
  const list = el('project-list');
  if (!ready.length) {
    list.innerHTML = '<p class="muted small">Nenhuma produção com plano de imagens pronto. Aprove os ganchos e gere o plano primeiro.</p>';
    return;
  }
  list.innerHTML = ready.map(p => `<label class="project-pick"><input type="checkbox" value="${p.id}">
    <span><b>${p.avatar || 'Avatar'}</b><span class="muted small">${p.title}</span></span></label>`).join('');
  list.addEventListener('change', () => {
    el('build-queue').disabled = !list.querySelectorAll('input:checked').length;
  });
}

async function buildQueue() {
  const ids = [...document.querySelectorAll('#project-list input:checked')].map(i => i.value);
  const { steps } = await api('/api/console/queue', { ids });
  if (!steps.length) { alert('As produções escolhidas não têm plano de imagens.'); return; }
  state.steps = steps;
  state.index = 0;
  el('picker').hidden = true;
  el('runner').hidden = false;
  render();
}

function render() {
  const step = state.steps[state.index];
  if (!step) return;
  el('step-avatar').textContent = step.avatar;
  el('step-role').textContent = (step.role || '').toUpperCase();
  el('step-id').textContent = step.id;
  el('step-title').textContent = step.frame_title || '';
  el('step-action').textContent = step.action;
  el('step-action').className = 'step-action ' + (step.action.startsWith('EDITAR') ? 'is-edit' : 'is-new');
  el('step-hint').textContent = step.hint + (step.takes?.length ? ` Takes: ${step.takes.join(', ')}.` : '');
  el('step-prompt').textContent = step.prompt;
  el('step-index').textContent = step.index + 1;
  el('step-total').textContent = step.total;
  el('queue-progress').max = step.total;
  el('queue-progress').value = step.index + 1;
  el('queue-count').textContent = `${step.index + 1} de ${step.total} · ${step.avatar}`;
  el('attach-block').innerHTML = step.attach.length
    ? '<div class="eyebrow">ANEXAR NESTE PASSO</div>' + step.attach.map((a, i) =>
        `<div class="attach-row"><span><b>${a.label}</b><span class="muted small">${a.path}</span></span>
         <button class="secondary" data-attach="${i}">⧉ Copiar arquivo</button></div>`).join('')
    : '<p class="muted small">Nada a anexar neste passo.</p>';
  copyPrompt(true);
}

async function copyPrompt(silent) {
  const step = state.steps[state.index];
  try {
    await navigator.clipboard.writeText(step.prompt);
    if (!silent) flash('Prompt copiado.');
  } catch { if (!silent) flash('Copie manualmente do quadro abaixo.'); }
}

async function copyAttachment(i) {
  const step = state.steps[state.index];
  try {
    await api('/api/console/clipboard', { path: step.attach[i].path });
    flash('Arquivo na área de transferência, cole no ChatGPT com Ctrl+V.');
  } catch (e) { flash(e.message); }
}

function flash(message) {
  const box = el('watch-status');
  box.textContent = message;
  box.classList.add('is-flash');
  setTimeout(() => box.classList.remove('is-flash'), 1600);
}

async function toggleWatch() {
  const step = state.steps[state.index];
  if (state.watching) {
    await api('/api/console/watch/stop', {});
    state.watching = false;
    el('watch-toggle').textContent = '◎ Aguardar download';
    flash('Arquivamento parado.');
    return;
  }
  await api('/api/console/watch', { step });
  state.watching = true;
  el('watch-toggle').textContent = '■ Parar de aguardar';
  flash(`Aguardando a imagem de ${step.id} cair em Downloads.`);
  poll();
}

async function poll() {
  if (!state.watching) return;
  const data = await api('/api/console/watch').catch(() => null);
  if (data) {
    renderFiled(data.filed);
    if (!data.running) {
      state.watching = false;
      el('watch-toggle').textContent = '◎ Aguardar download';
      if (data.result?.filed) { flash('Arquivado. Avançando.'); next(); }
      else if (data.result?.error) flash('Falha ao arquivar: ' + data.result.error);
      else flash('Espera encerrada sem novo arquivo.');
      return;
    }
  }
  setTimeout(poll, 1500);
}

function renderFiled(filed) {
  el('filed-list').innerHTML = (filed || []).map(f =>
    `<li><b>${f.id}</b> <span class="muted small">${f.avatar}</span> <span class="muted small">${f.path}</span></li>`).join('');
}

function next() { if (state.index < state.steps.length - 1) { state.index++; render(); } else flash('Fila concluída.'); }
function prev() { if (state.index > 0) { state.index--; render(); } }

document.addEventListener('click', e => {
  const attach = e.target.closest('[data-attach]');
  if (attach) return copyAttachment(Number(attach.dataset.attach));
  if (e.target.id === 'build-queue') return buildQueue();
  if (e.target.id === 'copy-prompt') return copyPrompt(false);
  if (e.target.id === 'watch-toggle') return toggleWatch();
  if (e.target.id === 'next-step') return next();
  if (e.target.id === 'prev-step') return prev();
});

document.addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.key === 'ArrowRight') next();
  if (e.key === 'ArrowLeft') prev();
  if (e.key === 'c' && !e.ctrlKey && !e.metaKey) copyPrompt(false);
});

loadProjects();
