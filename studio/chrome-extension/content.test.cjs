const {test}=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const fs=require('node:fs');
const path=require('node:path');
const code=fs.readFileSync(path.join(__dirname,'content.js'),'utf8');
function fixture({text='AURALY_IMAGE_JOB_abc',draft='',images=[],busy=false,replies=[]}={}){
  const edit={textContent:draft};
  const root={innerText:text,querySelector:s=>busy&&s==='[data-testid=stop-button]'?{}:null,
    querySelectorAll:s=>s==='[data-message-author-role="assistant"]'?replies:s.startsWith('img[alt^=')?images:[]};
  const sandbox={console,setTimeout,URL,location:{pathname:'/c/test-123',origin:'https://chatgpt.com'},
    document:{querySelector:s=>s==='main'?root:s.startsWith('#prompt-textarea')?edit:null},
    chrome:{runtime:{id:'extension',onMessage:{addListener(){}}}}};
  vm.createContext(sandbox);vm.runInContext(code,sandbox);return sandbox;
}
const image={src:'https://chatgpt.com/backend-api/estuary/content?id=observed',currentSrc:'https://chatgpt.com/backend-api/estuary/content?id=observed',complete:true,naturalWidth:941,naturalHeight:1672};
test('current ChatGPT generated image without assistant role is received',async()=>{
  const r=await fixture({images:[image]}).inspect({id:'abc'});assert.equal(r.kind,'image');assert.equal(r.src,image.src);
});
test('unrelated conversation never supplies a result',async()=>{
  await assert.rejects(()=>fixture({text:'other conversation',images:[image]}).inspect({id:'abc'}),/não corresponde/);
});
test('unfinished stream does not advance even with loaded preview',async()=>{
  assert.equal((await fixture({images:[image],busy:true}).inspect({id:'abc'})).kind,'waiting');
});
test('multiple results require review',async()=>{
  await assert.rejects(()=>fixture({images:[image,{...image,src:image.src+'2'}]}).inspect({id:'abc'}),/Mais de uma/);
});
test('draft after uncertain submit is not sent a second time',async()=>{
  await assert.rejects(()=>fixture({draft:'AURALY_IMAGE_JOB_abc'}).inspect({id:'abc'}),/incerto/);
});
test('quota message becomes actionable pause',async()=>{
  await assert.rejects(()=>fixture({text:'AURALY_IMAGE_JOB_abc Você atingiu o limite'}).inspect({id:'abc'}),/limite/);
});
test('uploaded anchor alone is not a generated image',async()=>{
  assert.equal((await fixture().inspect({id:'abc'})).kind,'waiting');
});
