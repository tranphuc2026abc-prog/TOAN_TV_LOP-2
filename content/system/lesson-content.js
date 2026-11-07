/* Học liệu độc lập; giữ nguyên ID bài và dữ liệu tiến độ wl3:* hiện có. */
(function () {
  'use strict';
  var content = {}, previousBank = practiceBank, previousLesson = lesson;
  var previousStart = startQ, previousAns = ans, previousGames = gameQuestions;
  var previousGameFeedback = gamePlayWithFeedback, previousQuiz=quiz, previousGamePlay=gamePlay;
  var previousMini=answerMini, previousTF=answerTF, previousCheckPair=checkPair, previousGameResult=gameResult,previousMatchScreen=gameMatchScreen;
  function bankFor(id) {
    return content[id].practice.map(function (q) {
      return {id:id, question_id:q.question_id, type:q.type, prompt:q.question,
        answer:q.correct_answer, wrong:(q.options||q.distractors||[]).filter(function(a){return a!==q.correct_answer;}),
        explanation:q.explanation, difficulty:q.difficulty, figure:q.figure,
        reference_table:q.reference_table?content[id].reference_table:null};
    });
  }
  function sample(id) {
    var all=bankFor(id), out=[];
    [['nhan_biet',3],['thong_hieu',3],['van_dung',4]].forEach(function(pair){
      out=out.concat(shuf(all.filter(function(q){return q.difficulty===pair[0];})).slice(0,pair[1]));
    });
    return shuf(out);
  }
  practiceBank=function(l){return l&&content[l[0]]?bankFor(l[0]):previousBank(l);};
  startQ=function(id, mode){
    if(content[id]&&mode==null)mode='all';
    if(!content[id]||typeof mode!=='string')return previousStart(id,mode);
    var questions=mode==='all'?sample(id):shuf(bankFor(id).filter(function(q){return q.type===mode;})).slice(0,10);
    if(!questions.length){toast('Bài này hiện có trắc nghiệm và điền đáp án.');return;}
    go({p:'quiz',id:id,qs:questions,i:0,ok:0,t:0,done:0,fb:'',pick:null,opts:null});
  };
  ans=function(i){
    var q=v.qs&&v.qs[v.i];
    if(q&&q.explanation){
      if(v.done)return;
      previousAns(i);
      if(v.done){v.fb+=' '+esc(q.explanation);draw();}
      return;
    }
    return previousAns(i);
  };
  function list(items){return '<ul>'+items.map(function(s){return '<li>'+esc(s)+'</li>';}).join('')+'</ul>';}
  var drawing=null;
  var drawTasks={
    rectangle:{title:'Chữ nhật 4 ô × 2 ô',steps:'Chọn hai đỉnh đối diện của hình chữ nhật dài 4 ô, rộng 2 ô.',points:2},
    square:{title:'Hình vuông cạnh 3 ô',steps:'Chọn hai đỉnh đối diện của hình vuông có cạnh 3 ô.',points:2},
    circle:{title:'Đường tròn bán kính 2 ô',steps:'Chọn tâm trước, rồi chọn một điểm trên đường tròn. Đường tròn cần nằm trọn trong lưới.',points:2},
    angle:{title:'Góc vuông',steps:'Chọn đỉnh A trước, sau đó chọn điểm B trên một cạnh và điểm C trên cạnh còn lại.',points:3}
  };
  function drawCoordinates(p){return {x:25+p.x*45,y:25+p.y*45};}
  function renderDrawing(){
    var box=document.getElementById('geometryDraw');if(!box||!drawing)return;
    var task=drawTasks[drawing.mode],pts=drawing.points,shape='',grid='',dots='';
    for(var x=0;x<=10;x++)grid+='<path d="M'+(25+45*x)+' 25V295" stroke="#ccd8e8"/>';
    for(var y=0;y<=6;y++)grid+='<path d="M25 '+(25+45*y)+'H475" stroke="#ccd8e8"/>';
    if(pts.length>=2){
      var a=drawCoordinates(pts[0]),b=drawCoordinates(pts[1]);
      if(drawing.mode==='circle')shape='<circle cx="'+a.x+'" cy="'+a.y+'" r="'+Math.hypot(a.x-b.x,a.y-b.y)+'" fill="#cbecf6" fill-opacity=".45" stroke="#246ca8" stroke-width="3"/>';
      else if(drawing.mode==='angle'){
        var c=pts[2]&&drawCoordinates(pts[2]);
        shape='<path d="M'+b.x+' '+b.y+'L'+a.x+' '+a.y+(c?'L'+c.x+' '+c.y:'')+'" fill="none" stroke="#246ca8" stroke-width="3"/>';
      }else shape='<rect x="'+Math.min(a.x,b.x)+'" y="'+Math.min(a.y,b.y)+'" width="'+Math.abs(a.x-b.x)+'" height="'+Math.abs(a.y-b.y)+'" fill="#d6efdf" fill-opacity=".5" stroke="#258559" stroke-width="3"/>';
    }
    for(var gy=0;gy<=6;gy++)for(var gx=0;gx<=10;gx++)dots+='<circle id="geo-'+gx+'-'+gy+'" cx="'+(25+gx*45)+'" cy="'+(25+gy*45)+'" r="18" fill="none" stroke="none" pointer-events="all" stroke-width="3" style="cursor:pointer" onfocus="this.setAttribute(&quot;stroke&quot;,&quot;#f2aa28&quot;)" onblur="this.setAttribute(&quot;stroke&quot;,&quot;none&quot;)" role="button" tabindex="0" aria-label="Chọn điểm cột '+gx+', hàng '+gy+'" onclick="chooseGeometryPoint('+gx+','+gy+')" onkeydown="if(event.key===\'Enter\'||event.key===\' \'){event.preventDefault();chooseGeometryPoint('+gx+','+gy+')}"/><circle cx="'+(25+gx*45)+'" cy="'+(25+gy*45)+'" r="5" fill="#60758e" pointer-events="none"/>';
    pts.forEach(function(p,i){var c=drawCoordinates(p),label=drawing.mode==='circle'?(i?'P':'O'):drawing.mode==='angle'?['A','B','C'][i]:['A','C'][i];dots+='<circle cx="'+c.x+'" cy="'+c.y+'" r="6" fill="#dd7e26" pointer-events="none"/><text x="'+(c.x+(p.x===10?-19:8))+'" y="'+(c.y+(p.y===0?24:-10))+'" fill="#17345e" font-size="20" pointer-events="none">'+label+'</text>';});
    box.innerHTML='<h3>✏️ Luyện vẽ trên lưới</h3><p>Mỗi khoảng giữa hai chấm là 1 ô. Đây là lưới mô phỏng; số ô không phải số cm thật.</p><div>'+Object.keys(drawTasks).map(function(mode){return '<button type="button" aria-pressed="'+(mode===drawing.mode)+'" onclick="setGeometryMode(\''+mode+'\')">'+drawTasks[mode].title+'</button>';}).join(' ')+'</div><p>'+task.steps+'</p><div style="overflow-x:auto"><svg viewBox="0 0 500 320" style="width:100%;min-width:360px;max-width:600px;height:auto" role="group" aria-label="Lưới vẽ 10 ô ngang, 6 ô dọc"><rect width="500" height="320" fill="#fbfdff"/>'+grid+'<g pointer-events="none">'+shape+'</g>'+dots+'</svg></div><p role="status" aria-live="polite" id="geometryFeedback">'+esc(drawing.feedback||'Chọn điểm đầu tiên. Có thể dùng phím Tab và Enter để chọn các chấm.')+'</p><button type="button" onclick="setGeometryMode(\''+drawing.mode+'\')">Xóa nét, vẽ lại</button><p>Phần luyện vẽ giúp tự kiểm tra; không cộng sao hay XP.</p>';
  }
  window.setGeometryMode=function(mode){if(!drawTasks[mode])return;drawing={mode:mode,points:[],feedback:'',complete:false};renderDrawing();};
  window.chooseGeometryPoint=function(x,y){
    if(!drawing||!document.getElementById('geometryDraw')||!Number.isInteger(x)||!Number.isInteger(y)||x<0||x>10||y<0||y>6)return;
    if(drawing.complete)drawing={mode:drawing.mode,points:[],feedback:'',complete:false};
    if(drawing.points.some(function(p){return p.x===x&&p.y===y;})){drawing.feedback='Điểm này đã được chọn. Hãy chọn điểm khác.';renderDrawing();return;}
    drawing.points.push({x:x,y:y});var pts=drawing.points,task=drawTasks[drawing.mode];
    if(pts.length===task.points){
      var dx=Math.abs(pts[1].x-pts[0].x),dy=Math.abs(pts[1].y-pts[0].y),ok=false;
      if(drawing.mode==='rectangle'){ok=(dx===4&&dy===2)||(dx===2&&dy===4);drawing.feedback='Hai cạnh theo lưới dài '+dx+' ô và '+dy+' ô.';}
      if(drawing.mode==='square'){ok=dx===3&&dy===3;drawing.feedback='Hai cạnh theo lưới dài '+dx+' ô và '+dy+' ô.';}
      if(drawing.mode==='circle'){
        var radius=Math.hypot(dx,dy),inside=pts[0].x-radius>=0&&pts[0].x+radius<=10&&pts[0].y-radius>=0&&pts[0].y+radius<=6;
        ok=Math.abs(radius-2)<1e-9&&inside;drawing.feedback='Bán kính vừa chọn khoảng '+Math.round(radius*100)/100+' ô.'+(!inside?' Đường tròn vượt ra ngoài lưới.':'');
      }
      if(drawing.mode==='angle'){
        var u={x:pts[1].x-pts[0].x,y:pts[1].y-pts[0].y},w={x:pts[2].x-pts[0].x,y:pts[2].y-pts[0].y};
        ok=u.x*w.x+u.y*w.y===0;drawing.feedback=ok?'Hai cạnh tạo một góc vuông, kể cả khi xoay nghiêng.':'Hai cạnh chưa tạo góc vuông; thử chọn theo hàng/cột hoặc kiểm tra bằng ê ke.';
      }
      drawing.complete=true;drawing.feedback=(ok?'✅ Đạt yêu cầu. ':'💡 Chưa đúng yêu cầu. ')+drawing.feedback+' Chọn điểm mới để bắt đầu lại.';
    }else drawing.feedback='Đã chọn '+pts.length+'/'+task.points+' điểm. '+task.steps;
    renderDrawing();var focus=document.getElementById('geo-'+x+'-'+y);if(focus)focus.focus({preventScroll:true});
  };
  function activitiesHTML(items){return '<h3>🧰 Thực hành với dụng cụ</h3>'+items.map(function(a){return '<section><h4>'+esc(a.title)+'</h4><p>Dụng cụ: '+esc(a.materials.join(', '))+'.</p><ol>'+a.steps.map(function(s){return '<li>'+esc(s)+'</li>';}).join('')+'</ol><p>Tự kiểm tra:</p>'+list(a.check)+'</section>';}).join('');}
  function figureHTML(f){return '<figure><img style="width:100%;max-width:560px;height:auto" src="'+esc(f.path)+'" alt="'+esc(f.caption)+'"><figcaption>'+esc(f.caption)+'</figcaption></figure>';}
  function referenceTable(t){
    return '<div style="overflow-x:auto"><table style="border-collapse:collapse;text-align:center;width:100%"><caption>'+esc(t.caption)+'</caption><thead><tr><th scope="col">×</th>'+t.columns.map(function(n){return '<th scope="col" style="padding:8px;border:1px solid #ccd5e5">'+n+'</th>';}).join('')+'</tr></thead><tbody>'+t.rows.map(function(row){return '<tr><th scope="row" style="padding:8px;border:1px solid #ccd5e5">'+row.factor+'</th>'+row.values.map(function(n){return '<td style="padding:8px;border:1px solid #ccd5e5">'+n+'</td>';}).join('')+'</tr>';}).join('')+'</tbody></table></div>';
  }
  function showFigure(q){
    if(!q||(!q.figure&&!q.reference_table)||A.querySelector('[data-question]'))return;
    var heading=A.querySelector('.card h2')||A.querySelector('.card h3');
    if(heading){var node=document.createElement('div');node.innerHTML=(q.figure?figureHTML(q.figure):'')+(q.reference_table?referenceTable(q.reference_table):'');node.dataset.question='true';heading.insertAdjacentElement('afterend',node);}
  }
  quiz=function(){previousQuiz();showFigure(v.qs&&v.qs[v.i]);};
  lesson=function(){
    previousLesson();
    var c=content[v.id];if(!c)return;
    var card=A.querySelector('.kw-lesson-content')||A.querySelector('.card');if(!card)return;
    card.innerHTML='<h2>'+esc(c.title)+'</h2><p>'+esc(S[c.subject].n)+' · Tập '+esc(c.volume)+' · Trang '+c.source.printed_pages.join('–')+'</p>'+
      '<div class="note">Học liệu: '+c.practice.length+' câu. '+(c.verification.teacher_approved?'Giáo viên đã thẩm định.':'AI đã biên soạn và rà soát; đang chờ giáo viên thẩm định.')+'</div>'+
      '<h3>🎯 Mục tiêu</h3>'+list(c.objectives)+'<h3>🌟 Khám phá kiến thức</h3><p>'+esc(c.knowledge.introduction)+'</p>'+list(c.knowledge.rules)+
      '<h3>👣 Cách học</h3>'+list(c.knowledge.steps)+'<h3>💡 Ví dụ</h3>'+c.examples.map(function(e){return '<h4>'+esc(e.question)+'</h4>'+list(e.steps);}).join('')+
      '<h3>🔎 Lỗi thường gặp</h3>'+list(c.knowledge.common_errors)+(c.figures?'<h3>📐 Hình minh họa</h3>'+c.figures.map(figureHTML).join(''):'')+
      (c.reference_table?'<h3>🔢 Tra bảng</h3>'+referenceTable(c.reference_table):'')+
      (c.activities?activitiesHTML(c.activities):'')+(c.drawing_practice?'<section id="geometryDraw"></section>':'')+
      '<h3>🎯 Luyện tập</h3><p>Mỗi lượt 10 câu: 3 nhận biết, 3 thông hiểu, 4 vận dụng. Xem lời giải sau khi trả lời.</p>'+
      '<button class="big" onclick="startQ(\''+c.id+'\',\'all\')">Luyện tập 10 câu</button> '+
      '<button onclick="startQ(\''+c.id+'\',\'mcq\')">Trắc nghiệm</button> '+
      '<button onclick="startQ(\''+c.id+'\',\'fill\')">Điền đáp án</button>'+
      '<h3>🎮 '+esc(c.games[0].title)+'</h3><p>'+esc(c.games[0].objective)+'</p>'+list(c.games[0].rules)+
      '<button class="big" onclick="startLessonGame(\''+c.id+'\')">Bắt đầu trò chơi</button>'+
      '<h3>⭐ Tự đánh giá</h3><p>'+esc(c.assessment.scoring)+'</p><p>'+esc(c.assessment.review_advice)+'</p>';
    if(c.drawing_practice)window.setGeometryMode('rectangle');
  };
  gameQuestions=function(){
    var old=previousGames().filter(function(q){return !content[q.id];});
    Object.keys(content).forEach(function(id){old=old.concat(bankFor(id));});
    return old;
  };
  window.startLessonGame=function(id){
    if(!content[id])return;
    var saved=gameQuestions,mode=content[id].games[0].mode;
    try{
      gameQuestions=function(){
        if(mode==='speed')return shuf(bankFor(id));
        if(mode==='match'){
          var answers={},pairs=[];
          shuf(bankFor(id)).forEach(function(q){if(!answers[q.answer]&&pairs.length<5){answers[q.answer]=true;pairs.push(q);}});
          return pairs;
        }
        return sample(id);
      };
      startMini(mode);G.lessonContentId=id;
    }
    finally{gameQuestions=saved;}
  };
  gameResult=function(){
    previousGameResult();
    if(G&&G.lessonContentId){var button=A.querySelector('button.big');if(button)button.onclick=function(){startLessonGame(G.lessonContentId);};}
  };
  gamePlay=function(){previousGamePlay();if(G&&!G.ended&&G.mode!=='match')showFigure(G.mode==='tf'?G.current:G.all[G.idx%G.all.length]);};
  gameMatchScreen=function(){
    previousMatchScreen();if(!G||G.ended)return;
    var seen={},references=[];
    G.all.forEach(function(q){
      if(q.figure&&!seen[q.figure.path]){seen[q.figure.path]=true;references.push(figureHTML(q.figure));}
      if(q.reference_table&&!seen.table){seen.table=true;references.push(referenceTable(q.reference_table));}
    });
    if(references.length){var heading=A.querySelector('.card h2'),section=document.createElement('section');section.className='match-references';section.innerHTML='<h3>Hình và bảng dùng cho câu hỏi</h3>'+references.join('');if(heading)heading.insertAdjacentElement('afterend',section);}
  };
  answerMini=function(value){
    var q=G&&G.all&&G.all[G.idx%G.all.length],speed=G&&G.mode==='speed';
    previousMini(value);
    if(speed&&q&&q.explanation){var fb=A.querySelector('.fb');if(fb)fb.textContent=(String(value)===String(q.answer)?'✅ Chính xác. ':'💡 Đáp án: '+q.answer+'. ')+q.explanation;}
  };
  checkPair=function(){
    var q=G&&G.all&&G.all[G.pickQ],matched=G&&G.pickQ===G.pickA;
    previousCheckPair();
    if(matched&&q&&q.explanation)G.feedback+=' '+q.explanation;
  };
  gamePlayWithFeedback=function(){
    if(G&&G.all){var q=G.all[G.idx%G.all.length];if(q&&q.explanation)G.feedback+=' '+q.explanation;}
    return previousGameFeedback();
  };
  // Mỗi tệp lỗi độc lập: bài cũ vẫn mở được, có thể tải lại bằng cách nạp lại trang.
  function validate(c,entry){
    if(c.id!==entry.id||!S[c.subject]||!Array.isArray(c.practice)||c.practice.length!==entry.question_count||!c.knowledge||!c.verification||!c.games.length)throw Error('Học liệu không hợp lệ: '+entry.id);
    var seen={};c.practice.forEach(function(q){
      if(!q.question_id||seen[q.question_id]||!q.question||q.correct_answer==null||!q.explanation||['mcq','fill','tf'].indexOf(q.type)<0)throw Error('Câu hỏi không hợp lệ: '+c.id);
      if(q.type==='mcq'&&(!Array.isArray(q.options)||q.options.indexOf(q.correct_answer)<0||new Set(q.options).size!==q.options.length))throw Error('Lựa chọn không hợp lệ: '+q.question_id);
      seen[q.question_id]=true;
    });
  }
  window.lessonContentReady=fetch('content/system/INDEX.json').then(function(r){if(!r.ok)throw Error('INDEX');return r.json();}).then(function(index){
    return Promise.all(index.lessons.filter(function(e){return e.path&&e.question_count>0;}).map(function(entry){
      return fetch(entry.path).then(function(r){if(!r.ok)throw Error(entry.id);return r.json();}).then(function(c){validate(c,entry);content[c.id]=c;})
        .catch(function(e){console.warn('Giữ học liệu cũ do không tải được tệp:',e.message);});
    }));
  }).catch(function(e){console.warn('Giữ danh mục và bài học cũ:',e.message);}).then(function(){if(P)draw();return Object.keys(content);});
})();
