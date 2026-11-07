// npm install --prefix /tmp/class3-test jsdom; NODE_PATH=/tmp/class3-test/node_modules node scripts/test_batch1_dom.cjs
const {JSDOM,VirtualConsole}=require('jsdom');
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
async function boot(missing){
 const errors=[],console=new VirtualConsole();console.on('jsdomError',e=>errors.push(e.message));
 const dom=new JSDOM(fs.readFileSync(path.join(root,'index.html'),'utf8').replace('<script src="content/system/lesson-content.js"></script>',()=>'<script>'+fs.readFileSync(path.join(root,'content/system/lesson-content.js'),'utf8')+'</script>'),{url:'http://127.0.0.1:8765/',runScripts:'dangerously',resources:'usable',virtualConsole:console,beforeParse(w){
  w.scrollTo=()=>{};w.fetch=async url=>{const p=path.join(root,url);return {ok:!String(url).includes(missing||'NONE')&&fs.existsSync(p),json:async()=>JSON.parse(fs.readFileSync(p,'utf8'))};};
 }});
 await new Promise(r=>dom.window.addEventListener('load',r));await dom.window.lessonContentReady;
 return {w:dom.window,errors};
}
(async()=>{
 const {w,errors}=await boot();w.load('KiemThu');w.go({p:'home'});assert.equal(w.L.length,168);
 for(let n=1;n<=4;n++){
  const id='TOAN3_T1_B0'+n;w.go({p:'lesson',id});assert(w.A.textContent.includes('40 câu'));
  const sets=new Set();
  for(let k=0;k<8;k++){
   w.startQ(id,'all');assert.equal(w.v.qs.length,10);assert.equal(new Set(w.v.qs.map(q=>q.question_id)).size,10);
   for(const [level,count] of [['nhan_biet',3],['thong_hieu',3],['van_dung',4]])assert.equal(w.v.qs.filter(q=>q.difficulty===level).length,count);
   sets.add(w.v.qs.map(q=>q.question_id).sort().join(','));
  }assert(sets.size>1);
  for(let i=0;i<10;i++){
   const q=w.v.qs[w.v.i];if(q.type==='mcq')w.ans(w.v.opts.indexOf(q.answer));else{w.document.getElementById('an').value=q.answer;w.ans();}
   assert.equal(w.v.done,1);assert(w.A.textContent.includes(q.explanation));const score=w.v.ok;w.ans(0);assert.equal(w.v.ok,score);w.nextQ();
  }assert.equal(w.P.les[id],3);
  w.startLessonGame(id);assert.equal(w.G.all.length,10);assert(w.G.all.every(q=>q.id===id));w.answerMini(w.G.all[0].answer);assert.equal(w.G.score,10);assert(w.A.textContent.includes(w.G.all[0].explanation));
 }
 const saved=JSON.parse(w.localStorage.getItem('wl3:p:KiemThu'));assert.equal(Object.keys(saved.les).length,4);w.load('KiemThu');assert.equal(w.P.xp,saved.xp);
 w.close();assert.deepEqual(errors,[]);
 const fail=await boot('TOAN3_T1_B02.json');fail.w.load('Fallback');assert.equal((await fail.w.lessonContentReady).length,3);fail.w.go({p:'lesson',id:'TOAN3_T1_B02'});fail.w.startQ('TOAN3_T1_B02','all');assert(fail.w.v.qs.length>0);assert.deepEqual(fail.errors,[]);fail.w.close();
 console.log('PASS DOM: 168 bài, 4 kho × 40 câu, lượt 10 câu 3/3/4, 8 lượt thay đổi, đáp án/lời giải, chống chấm lặp, 4 trò chơi, lưu/nạp tiến độ, fallback 404. Chưa kiểm tra bố cục trình duyệt.');
})().catch(e=>{console.error(e);process.exit(1);});
