document.getElementById('connect').onclick = async () => {
  const token = document.getElementById('token').value.trim();
  if (token.length < 30) { document.getElementById('status').textContent='Cole o código exibido no Studio.'; return; }
  await chrome.storage.local.set({auralyToken:token});
  const result = await chrome.runtime.sendMessage({type:'wake'});
  document.getElementById('status').textContent=result?.error || 'Conectado. Inicie a fila no Auraly Studio.';
};
document.getElementById('studio').onclick=()=>chrome.tabs.create({url:'http://127.0.0.1:8766/browser'});
