/* Học liệu độc lập; giữ nguyên ID bài và dữ liệu tiến độ wl3:* hiện có. */
(function () {
  'use strict';
  var content = {}, previousBank = practiceBank, previousLesson = lesson;
  var previousStart = startQ, previousAns = ans, previousGames = gameQuestions;
  var previousGameFeedback = gamePlayWithFeedback, previousQuiz=quiz, previousGamePlay=gamePlay;
  var previousMini=answerMini, previousTF=answerTF, previousCheckPair=checkPair, previousGameResult=gameResult;
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
      '<h3>🎯 Luyện tập</h3><p>Mỗi lượt 10 câu: 3 nhận biết, 3 thông hiểu, 4 vận dụng. Xem lời giải sau khi trả lời.</p>'+
      '<button class="big" onclick="startQ(\''+c.id+'\',\'all\')">Luyện tập 10 câu</button> '+
      '<button onclick="startQ(\''+c.id+'\',\'mcq\')">Trắc nghiệm</button> '+
      '<button onclick="startQ(\''+c.id+'\',\'fill\')">Điền đáp án</button>'+
      '<h3>🎮 '+esc(c.games[0].title)+'</h3><p>'+esc(c.games[0].objective)+'</p>'+list(c.games[0].rules)+
      '<button class="big" onclick="startLessonGame(\''+c.id+'\')">Bắt đầu trò chơi</button>'+
      '<h3>⭐ Tự đánh giá</h3><p>'+esc(c.assessment.scoring)+'</p><p>'+esc(c.assessment.review_advice)+'</p>';
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
