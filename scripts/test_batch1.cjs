const {chromium}=require('playwright');
const assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
 const page=await browser.newPage(); const errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto('http://127.0.0.1:8765/');
 await page.evaluate(()=>lessonContentReady);
 await page.waitForFunction(()=>L.length===168);
 await page.evaluate(()=>{load('KiemThu');go({p:'home'});});
 for(let n=1;n<=4;n++){
  const id='TOAN3_T1_B0'+n;
  const result=await page.evaluate(id=>{
   go({p:'lesson',id});const displayed=A.textContent.includes('40 câu');
   startQ(id,'all');const distribution={};v.qs.forEach(q=>distribution[q.difficulty]=(distribution[q.difficulty]||0)+1);
   const ids=v.qs.map(q=>q.question_id);return {displayed,total:v.qs.length,distribution,unique:new Set(ids).size};
  },id);
  assert(result.displayed);assert.equal(result.total,10);assert.equal(result.unique,10);
  assert.deepEqual(result.distribution,{...result.distribution,nhan_biet:3,thong_hieu:3,van_dung:4});
  for(let j=0;j<10;j++){
   await page.evaluate(()=>{const q=v.qs[v.i];if(q.type==='mcq')ans(v.opts.indexOf(q.answer));else{document.getElementById('an').value=q.answer;ans();}});
   assert(await page.evaluate(()=>v.done===1&&A.textContent.includes(v.qs[v.i].explanation)));
   await page.evaluate(()=>nextQ());
  }
  assert.equal(await page.evaluate(id=>P.les[id],id),3);
  await page.evaluate(id=>startLessonGame(id),id);
  assert(await page.evaluate(id=>G.all.length===10&&G.all.every(q=>q.id===id),id));
  await page.evaluate(()=>answerMini(G.all[0].answer));
  assert.equal(await page.evaluate(()=>G.score),10);
  assert(await page.evaluate(()=>A.textContent.includes(G.all[0].explanation)));
 }
 const stored=await page.evaluate(()=>JSON.parse(localStorage.getItem('wl3:p:KiemThu')));
 assert.equal(Object.keys(stored.les).length,4);
 await page.reload();await page.evaluate(()=>lessonContentReady);
 assert.equal(await page.evaluate(()=>Object.keys(P.les).length),4);
 await page.setViewportSize({width:390,height:844});
 await page.evaluate(()=>go({p:'lesson',id:'TOAN3_T1_B01'}));
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
 await page.screenshot({path:'/tmp/batch1-mobile.png',fullPage:true});
 // Một file học liệu lỗi: giữ bài cũ, các bài khác vẫn tải được.
 await page.route('**/TOAN3_T1_B02.json',r=>r.fulfill({status:404,body:'missing'}));
 await page.reload();const loaded=await page.evaluate(()=>lessonContentReady);
 assert.equal(loaded.length,7);
 await page.evaluate(()=>{go({p:'lesson',id:'TOAN3_T1_B02'});startQ('TOAN3_T1_B02','all');});
 assert(await page.evaluate(()=>v.qs.length>0));
 assert.deepEqual(errors,[]);
 await browser.close();console.log('PASS: 4 bài × 10 câu, phân mức 3/3/4, lời giải, trò chơi, lưu/nạp tiến độ, mobile và fallback 404.');
})().catch(e=>{console.error(e);process.exit(1);});
