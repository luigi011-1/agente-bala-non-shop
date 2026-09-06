let batchSource=null, batchRequestId=null;
const batchDialog=document.createElement('dialog');
batchDialog.id='batch-dialog';
batchDialog.innerHTML=`<div class="dialog-heading"><div><div class="eyebrow">PRODUÇÃO EM LOTE</div><h2>Uma referência. Vários avatares.</h2></div><button id="batch-close" type="button">Fechar</button></div><p>A análise aprovada é reutilizada. Cada avatar recebe roteiro, âncora e imagens separados. Até dois projetos executam simultaneamente.</p><div id="batch-avatars"></div><label>Variações de gancho por avatar<input id="batch-count" type="number" min="1" max="5" value="3"></label><p class="small muted">Limite inicial por avatar: 100 chamadas de texto e 32 de imagem, incluindo falhas. Não é teto monetário. Prepare os roteiros e revise antes de autorizar as imagens.</p><button id="batch-create" class="primary">Criar lote e preparar roteiros</button><div id="batch-results"></div><p id="batch-message" class="small"></p>`;
document.body.append(batchDialog);
document.querySelector('#batch-close').onclick=()=>batchDialog.close();
async function showBatch(source){
 batchSource=source;batchRequestId=crypto.randomUUID();
 document.querySelector('#batch-avatars').innerHTML=state.config.avatars.map(a=>`<label><input type="checkbox" data-batch-avatar="${escape(a.id)}"> ${escape(a.name)}</label>`).join('');
 batchDialog.showModal();await refreshBatch();
}
async function refreshBatch(){
 if(!batchDialog.open||!batchSource)return;
 const all=await api('/projects');const children=all.filter(p=>p.batch_source===batchSource);
 const groups=Object.groupBy?Object.groupBy(children,p=>p.batch_id):children.reduce((r,p)=>{(r[p.batch_id]??=[]).push(p);return r;},{});
 document.querySelector('#batch-results').innerHTML=Object.entries(groups).map(([id,ps])=>`<div class="panel"><h3>${ps.length} avatares · Lote ${escape(id.slice(0,8))}</h3>${ps.map(p=>`<p><button data-project="${p.id}">${escape(p.avatar)} ↗</button> ${escape(p.queue_state||p.status)} · ${escape(p.active_text_provider||'aguardando')}<br><span class="small">${escape(p.progress||'Pronto para iniciar')}${p.error?' — '+escape(p.error):''}</span>${p.status==='complete'?`<br><a href="${fileURL('auraly-flow.zip',p.id)}" download>↓ ZIP deste avatar</a>`:''}</p>`).join('')}<p class="small">Autorizar produção aprova os roteiros atuais, seleciona os primeiros ganchos ordenados por congruência e gera/revisa as imagens. Abra cada avatar acima para revisar/editar antes.</p><button data-batch-run="${escape(id)}">Autorizar produção / retomar lote</button> <button data-batch-prepare="${escape(id)}">Retomar roteiros</button> <button data-batch-pause="${escape(id)}">Pausar lote</button></div>`).join('');
}
document.querySelector('#batch-create').onclick=async()=>{
 const button=document.querySelector('#batch-create');button.disabled=true;
 try{
 const avatars=[...document.querySelectorAll('[data-batch-avatar]:checked')].map(e=>e.dataset.batchAvatar);
 const result=await api(`/projects/${batchSource}/batch`,{avatars,variations:Number(document.querySelector('#batch-count').value),request_id:batchRequestId});
 await api('/batches/run',{ids:result.ids,produce:false});
 batchRequestId=crypto.randomUUID();await refreshBatch();
 }catch(e){document.querySelector('#batch-message').textContent=e.message;}finally{button.disabled=false;}
};
batchDialog.addEventListener('click',async e=>{
 const b=e.target.closest('button');if(!b)return;
 if(b.dataset.project){batchDialog.close();return;}
 const id=b.dataset.batchRun||b.dataset.batchPrepare||b.dataset.batchPause;if(!id)return;
 b.disabled=true;
 try{
 const all=await api('/projects');const ids=all.filter(p=>p.batch_source===batchSource&&p.batch_id===id).map(p=>p.id);
 if(b.dataset.batchRun&&!confirm(`Autorizar os roteiros atuais e produzir ${ids.length} avatares? Até ${ids.length*32} chamadas de imagem e ${ids.length*100} de texto nos limites iniciais cumulativos. Haverá cobrança nas contas dos provedores.`))return;
 await api(b.dataset.batchPause?'/batches/pause':'/batches/run',{ids,produce:!!b.dataset.batchRun});await refreshBatch();
 }catch(error){document.querySelector('#batch-message').textContent=error.message;}finally{b.disabled=false;}
});
setInterval(()=>refreshBatch().catch(()=>{}),3000);
