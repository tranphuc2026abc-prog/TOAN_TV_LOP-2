/* Học liệu độc lập; giữ nguyên ID bài và dữ liệu tiến độ wl3:* hiện có. */
(function () {
  'use strict';
  var content = {}, previousBank = practiceBank, previousLesson = lesson;
  var previousStart = startQ, previousAns = ans, previousGames = gameQuestions;
  var previousGameFeedback = gamePlayWithFeedback;
  function bankFor(id) {
    return content[id].practice.map(function (q) {
      return {id:id, question_id:q.question_id, type:q.type, prompt:q.question,
        answer:q.correct_answer, wrong:(q.options||[]).filter(function(a){return a!==q.correct_answer;}),
        explanation:q.explanation, difficulty:q.difficulty};
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
  lesson=function(){
    previousLesson();
    var c=content[v.id];if(!c)return;
    var card=A.querySelector('.kw-lesson-content')||A.querySelector('.card');if(!card)return;
    card.innerHTML='<h2>'+esc(c.title)+'</h2><p>Toán 3 · Tập 1 · Trang '+c.source.printed_pages.join('–')+'</p>'+
      '<div class="note">Học liệu mới: 40 câu. AI đã biên soạn và rà soát; đang chờ giáo viên thẩm định.</div>'+
      '<h3>🎯 Mục tiêu</h3>'+list(c.objectives)+'<h3>🌟 Khám phá kiến thức</h3><p>'+esc(c.knowledge.introduction)+'</p>'+list(c.knowledge.rules)+
      '<h3>👣 Cách học</h3>'+list(c.knowledge.steps)+'<h3>💡 Ví dụ</h3>'+c.examples.map(function(e){return '<h4>'+esc(e.question)+'</h4>'+list(e.steps);}).join('')+
      '<h3>🔎 Lỗi thường gặp</h3>'+list(c.knowledge.common_errors)+
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
    var saved=gameQuestions;
    try{gameQuestions=function(){return sample(id);};startMini('treasure');}
    finally{gameQuestions=saved;}
  };
  gamePlayWithFeedback=function(){
    if(G&&G.all){var q=G.all[G.idx%G.all.length];if(q&&q.explanation)G.feedback+=' '+q.explanation;}
    return previousGameFeedback();
  };
  // Mỗi tệp lỗi độc lập: bài cũ vẫn mở được, có thể tải lại bằng cách nạp lại trang.
  window.lessonContentReady=Promise.all([1,2,3,4].map(function(n){
    var id='TOAN3_T1_B0'+n;
    return fetch('content/toan/tap-1/'+id+'.json').then(function(r){if(!r.ok)throw Error(id);return r.json();}).then(function(c){
      if(c.id!==id||!Array.isArray(c.practice)||c.practice.length!==40||!c.knowledge)throw Error('Học liệu không hợp lệ: '+id);
      content[id]=c;
      var l=byId(id);if(l)l[9]=c.practice.map(function(q){return [q.question,q.correct_answer,(q.options||[]).filter(function(a){return a!==q.correct_answer;})];});
    }).catch(function(e){console.warn('Giữ học liệu cũ do không tải được tệp:',e.message);});
  })).then(function(){if(P)draw();return Object.keys(content);});
})();
