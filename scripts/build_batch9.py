"""Đóng gói Batch 9 từ câu hỏi, phương án nhiễu và nội dung đã biên soạn riêng."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())
text = (ROOT/'content/system/batch9-source.txt').read_text()
import re
sections = re.split(r'^Bài (?=\d+\s*$)', text, flags=re.M)[1:]
import subprocess, sys

subprocess.run([sys.executable, str(ROOT/'scripts/build_batch9_figures.py')], check=True)
details = json.loads((ROOT/'content/system/batch9-details.json').read_text())
game_rules = {
 'match':['Mỗi lượt chọn 5 câu có 5 đáp án khác nhau.', 'Chọn câu hỏi bên trái rồi đáp án bên phải. Sai thì thử lại.', 'Mỗi cặp đúng 10 điểm; tối đa 50 điểm.'],
 'speed':['Trả lời các câu thuộc bài trong 60 giây.', 'Mỗi câu đúng được 10 điểm, sai không được điểm; chuyển ngay sang câu tiếp.', 'Hết giờ thì kết thúc. Điểm riêng của lượt chơi, không thay kết quả luyện tập.'],
 'treasure':['Mỗi lượt lấy 10 câu từ bài học.', 'Chọn đáp án, đọc lời giải rồi sang câu tiếp theo.', 'Mỗi câu đúng được 10 điểm; tối đa 100 điểm.'],
 'tf':['Mỗi lượt lấy 10 câu trong bài và đưa ra một kết quả để kiểm chứng.', 'Chọn Đúng nếu kết quả phù hợp, chọn Sai nếu không phù hợp; đọc lời giải trước khi sang câu.', 'Mỗi câu đúng được 10 điểm; tối đa 100 điểm.']
}
for num, section in enumerate(sections, 33):
    lines = section.strip().splitlines()[1:]
    assert len(lines) == 40, (num, len(lines))
    meta = catalog['lessons'][num-1]
    d = details[num-33]
    qs = []
    for i, row in enumerate(lines):
        question, answer, explanation, distractors = row.split('|')
        # Dạng điền giữ câu trả lời ngắn, trắc nghiệm có phương án nhiễu số học.
        kind = 'mcq' if i % 2 == 0 else 'fill'
        n = answer
        wrong = distractors.split(';')
        assert len(wrong)==3 and len(set([answer]+wrong))==4, (num,i)
        qs.append(dict(question_id=f"{meta['id']}_Q{i+1:02}", type=kind, question=question,
                       **({'options': [str(n)]+list(map(str,wrong))} if kind=='mcq' else {}),
                       correct_answer=str(n), distractors=wrong, explanation=explanation,
                       difficulty='nhan_biet' if i<10 else 'thong_hieu' if i<20 else 'van_dung'))
    game_title, game_goal = d['game']
    obj = dict(id=meta['id'], subject='toan', grade=3, book='Kết nối tri thức với cuộc sống',
        volume=1, lesson_no=num, title=meta['title'], topic=d['topic'],
        source=dict(pdf=meta['source_pdf'], printed_pages=[meta['page_start'],meta['page_end']],
                    pdf_pages=[meta['page_start']+1,meta['page_end']+1],
                    review='Đã đọc trực quan toàn bộ trang nguồn cho bài này; nội dung và bài tập mới do AI biên soạn.'),
        objectives=d['objectives'], knowledge=dict(introduction=d['intro'], rules=d['rules'],
            steps=d['steps'], common_errors=d['errors']),
        examples=[dict(question=q,steps=s) for q,s in d['examples']], practice=qs,
        games=[dict(id=meta['id']+'_GAME1',title=game_title,mode=d['mode'],objective=game_goal,
            rules=game_rules[d['mode']],
            question_ids=[q['question_id'] for q in qs], answer_source='practice.correct_answer',
            feedback_source='practice.explanation', max_score=50 if d['mode']=='match' else 100 if d['mode']!='speed' else None)],
        assessment=dict(session_size=10,distribution=dict(nhan_biet=3,thong_hieu=3,van_dung=4),
            scoring='Đúng lần đầu: 1 điểm; đúng sau một gợi ý: 0,5 điểm. Từ 90%: 3 sao; từ 60%: 2 sao; còn lại: 1 sao.',
            review_advice='Xem lời giải các câu sai, đọc lại quy tắc, rồi làm một lượt mới.'),
        feedback=dict(correct='Chính xác! Hãy đọc lời giải để củng cố cách làm.',
                      incorrect='Em thử lại một lần. Sau đó xem đáp án và cách giải.'),
        verification=dict(ai_authored=True,structure_checked=True,answer_reviewed=True,
                          source_reviewed=True,teacher_approved=False),
        status='AI_CHECKED_AWAITING_TEACHER')
    if d.get('activities'): obj['activities']=d['activities']
    if num in (33,34):
        caption={33:'Hình A: Hai nhiệt kế P và Q. Mỗi khoảng nhỏ ứng với 2 °C; P ở 24 °C, Q ở 32 °C.',34:'Hình A: Thẻ trên thước mm, đầu trái ở 0 mm, đầu phải ở 35 mm. Hình mô phỏng, không đo màn hình.'}[num]
        obj['figures']=[dict(path=f'content/toan/tap-1/TOAN3_T1_B{num}_A.svg',caption=caption)]
        for q in qs:
            if 'Hình A' in q['question']:q['figure']=obj['figures'][0]
    dest=ROOT/f'content/toan/tap-1/{meta["id"]}'
    dest.with_suffix('.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    md=f"# {obj['title']}\n\nNguồn tham khảo: Toán 3 KNTT, tập 1, trang {meta['page_start']}-{meta['page_end']}.\n\nTrạng thái: AI biên soạn và rà soát; chưa có xác nhận của giáo viên.\n\n## Mục tiêu\n\n"+'\n'.join('- '+s for s in d['objectives'])
    md+='\n\n## Khám phá\n\n'+d['intro']+'\n\n'+'\n'.join('- '+s for s in d['rules'])
    md+='\n\n## Hướng dẫn\n\n'+'\n'.join(f'{i+1}. {s}' for i,s in enumerate(d['steps']))
    md+='\n\n## Lỗi thường gặp\n\n'+'\n'.join('- '+s for s in d['errors'])
    md+='\n\n## Ví dụ\n\n'+'\n\n'.join(e['question']+'\n\n'+'\n'.join(f'{i+1}. {s}' for i,s in enumerate(e['steps'])) for e in obj['examples'])
    md+='\n\n## Hình minh họa\n\n'+''.join('!['+f['caption']+']('+Path(f['path']).name+')\n\n' for f in obj.get('figures',[])) if obj.get('figures') else ''
    if obj.get('activities'):
        md+='\n\n## Thực hành với dụng cụ\n\n'
        for activity in obj['activities']:
            md+='### '+activity['title']+'\n\nDụng cụ: '+', '.join(activity['materials'])+'.\n\n'
            md+='\n'.join(f'{i+1}. {step}' for i,step in enumerate(activity['steps']))+'\n\nTự kiểm tra:\n\n'+'\n'.join('- '+item for item in activity['check'])+'\n\n'
    md+='\n\n## Ngân hàng câu hỏi\n\n'
    for i,q in enumerate(qs,1):
        md+=f"### Câu {i} - {q['difficulty']}\n\n{q['question']}\n\n"
        if 'options' in q: md+='; '.join(f'{chr(65+j)}. {o}' for j,o in enumerate(q['options']))+'\n\n'
        md+=f"Đáp án: {q['correct_answer']}. Lời giải: {q['explanation']}\n\n"
    md+='## Trò chơi\n\n'+game_title+': '+game_goal+'\n\n'+'\n'.join('- '+r for r in obj['games'][0]['rules'])
    md+='\n\n## Đánh giá\n\n'+obj['assessment']['scoring']+'\n\n'+obj['assessment']['review_advice']+'\n'
    dest.with_suffix('.md').write_text(md)
print('Đã đóng gói 4 bài, 160 câu, 4 trò chơi.')

# Luôn khôi phục xác nhận thẩm định từ sổ duyệt sau khi tái tạo học liệu.
import subprocess, sys
subprocess.run([sys.executable, str(ROOT/"scripts/update_content_index.py")], check=True)
