// Từ gốc repository: npm ci && npm test. Không phụ thuộc thư mục tạm.
const {JSDOM,VirtualConsole}=require('jsdom');
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const activeEntries=JSON.parse(fs.readFileSync(path.join(root,'content/system/INDEX.json'),'utf8')).lessons.filter(e=>e.path);
const activeCount=activeEntries.length;
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
 for(const entry of activeEntries){
  const id=entry.id,n=Number(id.slice(-2));w.go({p:'lesson',id});assert(w.A.textContent.includes('40 câu'));
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
  w.startQ(id);assert.equal(w.v.qs.length,10);
  w.startLessonGame(id);assert(w.G.all.every(q=>q.id===id));
  if(w.G.mode==='match'){
   assert.equal(w.G.pairs.length,5);assert.equal(new Set(w.G.pairs.map(q=>q.answer)).size,5);
   for(let j=0;j<5;j++){w.pickPair(0,j);w.pickPair(1,j);}assert.equal(w.G.score,50);assert(w.G.ended);
   w.A.querySelector('button.big').click();assert.equal(w.G.lessonContentId,id);
  }else if(w.G.mode==='tf'){
   assert.equal(w.G.all.length,10);w.answerTF(w.G.statementCorrect);assert.equal(w.G.score,10);assert(w.A.textContent.includes(w.G.all[0].explanation));
  }else{
   assert.equal(w.G.all.length,w.G.mode==='speed'?40:10);w.answerMini(w.G.all[0].answer);assert.equal(w.G.score,10);assert(w.A.textContent.includes(w.G.all[w.G.mode==='speed'?0:w.G.idx].explanation));
   if(w.G.mode==='speed')w.finishMini();
  }
  if(n<=4){w.go({p:'lesson',id});assert(w.A.textContent.includes('Giáo viên đã thẩm định'));}
  if(n===12){w.startQ(id,'all');w.v.qs=[w.practiceBank(w.byId(id)).find(q=>q.reference_table)];w.v.i=0;w.draw();assert.equal(w.A.querySelectorAll('tbody tr').length,8);assert.equal(w.A.querySelectorAll('tbody td').length,80);}
  if(n>=14){for(const question of w.practiceBank(w.byId(id)).filter(q=>q.figure)){w.startQ(id,'all');w.v.qs=[question];w.v.i=0;w.draw();assert(w.A.querySelector('figure img').getAttribute('src')===question.figure.path);}}
  if(n===7){w.startQ(id,'all');w.v.qs=[w.practiceBank(w.byId(id)).find(q=>q.figure)];w.v.i=0;w.draw();assert(w.A.querySelector('figure img'));}

 }
 if(activeEntries.some(e=>e.id==='TOAN3_T1_B20')){
  w.go({p:'lesson',id:'TOAN3_T1_B20'});assert(w.document.getElementById('geometryDraw'));assert(w.A.textContent.includes('Thực hành với dụng cụ'));
  const cases=[
   ['rectangle',[[0,0],[4,2]],true],['rectangle',[[0,0],[4,4]],false],
   ['square',[[1,1],[4,4]],true],['square',[[1,1],[4,3]],false],
   ['circle',[[3,3],[5,3]],true],['circle',[[0,0],[2,0]],false],
   ['angle',[[3,3],[1,1],[5,1]],true],['angle',[[3,3],[4,3],[4,4]],false]
  ];
  for(const [mode,points,correct] of cases){w.setGeometryMode(mode);for(const p of points)w.chooseGeometryPoint(...p);assert.equal(w.document.getElementById('geometryFeedback').textContent.startsWith('✅'),correct);}
  w.setGeometryMode('circle');w.document.getElementById('geo-3-3').dispatchEvent(new w.KeyboardEvent('keydown',{key:'Enter',bubbles:true}));w.document.getElementById('geo-5-3').dispatchEvent(new w.MouseEvent('click',{bubbles:true}));assert(w.document.getElementById('geometryFeedback').textContent.startsWith('✅'));
  w.setGeometryMode('square');w.chooseGeometryPoint(1,1);w.chooseGeometryPoint(1,1);assert(w.document.getElementById('geometryFeedback').textContent.includes('đã được chọn'));
  w.setGeometryMode('angle');assert(w.document.getElementById('geometryFeedback').textContent.includes('đầu tiên'));
  fs.writeFileSync('/tmp/geometry-board-preview.svg',w.document.querySelector('#geometryDraw svg').outerHTML.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" '));
 }
 // Các câu phụ thuộc hình/bảng phải đủ dữ kiện ngay cả trong trò ghép đôi.
 for(const id of ['TOAN3_T1_B19','TOAN3_T1_B12','TOAN3_T1_B24']){
  if(!activeEntries.some(e=>e.id===id))continue;
  const bank=w.practiceBank(w.byId(id)),media=bank.find(q=>q.figure||q.reference_table),chosen=[media],answers=new Set([media.answer]);
  for(const q of bank){if(chosen.length===5)break;if(!answers.has(q.answer)){answers.add(q.answer);chosen.push(q);}}
  const old=w.gameQuestions;w.gameQuestions=()=>chosen;w.startMini('match');w.gameQuestions=old;
  assert(w.A.querySelector('.match-references'));assert(w.A.querySelector(media.figure?'.match-references img':'.match-references table'));
 }
 // Kiểm tra nhận lại đáp án sau một lần sai và giải thích sau hai lần sai.
 w.startQ('TOAN3_T1_B12','fill');w.document.getElementById('an').value='sai';w.ans();assert.equal(w.v.done,0);assert.equal(w.v.t,1);
 w.document.getElementById('an').value=w.v.qs[0].answer;w.ans();assert.equal(w.v.ok,0.5);
 w.startQ('TOAN3_T1_B12','fill');for(let k=0;k<2;k++){w.document.getElementById('an').value='sai';w.ans();}assert.equal(w.v.done,2);assert(w.A.textContent.includes(w.v.qs[0].explanation));
 const saved=JSON.parse(w.localStorage.getItem('wl3:p:KiemThu'));assert.equal(Object.keys(saved.les).length,activeCount);w.load('KiemThu');assert.equal(w.P.xp,saved.xp);
 w.close();assert.deepEqual(errors,[]);
 const fail=await boot('TOAN3_T1_B02.json');fail.w.load('Fallback');assert.equal((await fail.w.lessonContentReady).length,activeCount-1);fail.w.go({p:'lesson',id:'TOAN3_T1_B02'});fail.w.startQ('TOAN3_T1_B02','all');assert(fail.w.v.qs.length>0);assert.deepEqual(fail.errors,[]);fail.w.close();
 console.log('PASS DOM: 168 bài, '+activeCount+' kho học liệu, lượt 10 câu 3/3/4 và nút làm lại, 8 lượt thay đổi, lời giải, chống chấm lặp, 4 loại trò chơi đúng phạm vi bài, hình minh họa, trạng thái thẩm định, lưu/nạp tiến độ, fallback 404. Chưa kiểm tra bố cục trình duyệt.');
})().catch(e=>{console.error(e);process.exit(1);});
