const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');

function harness(states){
  let reads=0,pings=0;
  const context=vm.createContext({
    URL,Uint8Array,Set,Date,
    setTimeout:fn=>{fn();return 1;},setInterval:()=>{},
    chrome:{
      storage:{local:{get:async()=>({})}},
      tabs:{get:async()=>states[Math.min(reads++,states.length-1)],
            sendMessage:async()=>{pings++;return {ready:true};}},
      runtime:{onMessage:{addListener:()=>{}}},
      alarms:{create:()=>{},onAlarm:{addListener:()=>{}}}
    }
  });
  vm.runInContext(fs.readFileSync(__dirname+'/background.js','utf8'),context);
  return {run:()=>vm.runInContext('waitTab(123)',context),counts:()=>({reads,pings})};
}
test('new tab waits through missing URL until ChatGPT is committed',async()=>{
  const h=harness([{status:'loading'}, {url:'',pendingUrl:'https://chatgpt.com/',status:'loading'},
                   {url:'https://chatgpt.com/',status:'complete'}]);
  await h.run();assert.deepEqual(h.counts(),{reads:3,pings:1});
});
test('about blank is transient and never receives content messages',async()=>{
  const h=harness([{url:'about:blank',status:'complete'}, {url:'https://chatgpt.com/',status:'complete'}]);
  await h.run();assert.deepEqual(h.counts(),{reads:2,pings:1});
});
test('navigation outside ChatGPT is still rejected before messaging',async()=>{
  const h=harness([{url:'https://example.com/',status:'complete'}]);
  await assert.rejects(h.run(),/saiu do ChatGPT/);assert.equal(h.counts().pings,0);
});
test('missing URL times out without sending a prompt',async()=>{
  const h=harness([{status:'loading'}]);
  await assert.rejects(h.run(),/não ficou pronto/);assert.deepEqual(h.counts(),{reads:40,pings:0});
});
