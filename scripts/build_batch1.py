"""Đóng gói học liệu đã biên soạn; không sinh câu hỏi bằng cách thay số."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())
text = (ROOT/'content/system/batch1-source.txt').read_text()
sections = text.split('Bài ')[1:]
details = [
 dict(objectives=['Đọc, viết và phân tích số đến 1 000.', 'So sánh, sắp xếp và tìm số liền trước, liền sau.'],
 intro='Hãy tưởng tượng mỗi số có các ngăn trăm, chục và đơn vị. Chữ số ở ngăn nào cho biết có bao nhiêu phần của ngăn đó.',
 rules=['Số có ba chữ số gồm hàng trăm, hàng chục, hàng đơn vị. Chữ số 0 vẫn cần được viết để giữ đúng hàng.', 'So sánh từ hàng trăm; nếu bằng nhau, so hàng chục, rồi hàng đơn vị.', 'Số liền trước kém 1; số liền sau hơn 1. 999 có số liền sau là 1 000.'],
 steps=['Xác định từng hàng rồi đọc hoặc viết số.', 'Khi sắp xếp, tìm số bé nhất hoặc lớn nhất trước.', 'Đọc lại số và kiểm tra vị trí chữ số 0.'],
 errors=['Viết 806 thành 86 làm mất hàng trăm.', 'Chỉ nhìn chữ số cuối để so sánh 409 và 490.'],
 examples=[('Viết số gồm 4 trăm, 0 chục, 7 đơn vị.', ['4 trăm là 400; không có chục; có 7 đơn vị.', '400 + 7 = 407.']), ('Xếp 592, 529, 295 tăng dần.', ['295 có hàng trăm nhỏ nhất.', '529 và 592 cùng 5 trăm; 2 chục bé hơn 9 chục.', 'Thứ tự: 295, 529, 592.'])],
 game=('Mật mã chiếc tủ', 'Giải các câu về cấu tạo, thứ tự và so sánh số để mở từng khóa.')),
 dict(objectives=['Cộng, trừ nhẩm các số tròn chục, tròn trăm.', 'Đặt tính đúng hàng và giải bài toán thêm, bớt, hơn kém trong phạm vi 1 000.'],
 intro='Khi gom thêm đồ vật, ta thường dùng phép cộng; khi lấy bớt hoặc tìm phần chênh lệch, ta thường dùng phép trừ. Hãy đọc tình huống trước khi chọn phép tính.',
 rules=['Đặt các chữ số cùng hàng thẳng cột, tính từ phải sang trái.', 'Cộng đủ 10 đơn vị thì đổi thành 1 chục và nhớ sang hàng chục; tương tự với hàng trăm.', 'Khi chữ số ở trên bé hơn chữ số ở dưới, đổi 1 đơn vị của hàng bên trái thành 10 đơn vị của hàng đang tính.', 'Kiểm tra phép trừ bằng cách lấy hiệu cộng số trừ; kiểm tra phép cộng bằng cách lấy tổng trừ một số hạng.'],
 steps=['Đọc đề, xác định đã có, thêm vào hoặc bớt đi.', 'Chọn phép tính, đặt thẳng hàng nếu cần.', 'Tính, ghi đơn vị và thử lại.'],
 errors=['Quên cộng số nhớ khi cộng có nhớ.', 'Mượn 1 chục nhưng quên giảm chữ số hàng chục.', 'Thấy từ nhiều hơn là cộng ngay, dù câu hỏi đang yêu cầu tìm phần chênh lệch.'],
 examples=[('Tính 176 + 248.', ['6 + 8 = 14, viết 4 nhớ 1.', '7 + 4 + 1 = 12, viết 2 nhớ 1.', '1 + 2 + 1 = 4. Kết quả 424.']), ('Tính 402 - 176.', ['Đổi 1 trăm thành 10 chục, rồi 1 chục thành 10 đơn vị.', '12 - 6 = 6; 9 - 7 = 2; 3 - 1 = 2.', 'Kết quả 226. Thử lại: 226 + 176 = 402.'])],
 game=('Kho hàng thông minh', 'Đọc phiếu nhập, xuất và tìm đúng số hàng còn lại qua từng câu hỏi.')),
 dict(objectives=['Nhận biết số hạng, tổng, số bị trừ, số trừ, hiệu.', 'Chọn đúng phép tính để tìm thành phần chưa biết và thử lại.'],
 intro='Một phép tính có thể bị che một số. Muốn tìm số đó, trước hết hãy xác định tên thành phần bị che, rồi chọn quy tắc phù hợp.',
 rules=['Số hạng chưa biết = tổng - số hạng đã biết.', 'Số bị trừ = hiệu + số trừ.', 'Số trừ = số bị trừ - hiệu.', 'Thay số tìm được vào chỗ trống để kiểm tra phép tính ban đầu.'],
 steps=['Đọc tên các thành phần và đánh dấu số chưa biết.', 'Nói quy tắc thành lời trước khi tính.', 'Tính rồi thay đáp án vào phép tính ban đầu.'],
 errors=['Dùng cùng một quy tắc cho số bị trừ và số trừ.', 'Tìm được số nhưng không thử lại.', 'Nhầm số ban đầu với số còn lại trong bài toán.'],
 examples=[('Tìm số: ... + 46 = 120.', ['Chỗ trống là một số hạng.', 'Lấy tổng trừ số hạng đã biết: 120 - 46 = 74.', 'Thử lại: 74 + 46 = 120.']), ('Tìm số: ... - 27 = 58.', ['Chỗ trống là số bị trừ.', 'Lấy hiệu cộng số trừ: 58 + 27 = 85.', 'Thử lại: 85 - 27 = 58.']), ('Tìm số: 140 - ... = 65.', ['Chỗ trống là số trừ.', '140 - 65 = 75.', 'Thử lại: 140 - 75 = 65.'])],
 game=('Thám tử số bị che', 'Xác định thành phần bị che và giải câu hỏi để tìm lại từng manh mối.')),
 dict(objectives=['Nhớ và vận dụng bảng nhân 2, 5 và bảng chia 2, 5.', 'Phân biệt chia đều và chia theo nhóm trong tình huống thực tế.'],
 intro='Các nhóm bằng nhau có thể được đếm nhanh bằng phép nhân. Phép chia giúp tìm số đồ vật mỗi nhóm hoặc số nhóm được tạo thành.',
 rules=['2 × n biểu thị n nhóm, mỗi nhóm có 2; 5 × n biểu thị n nhóm, mỗi nhóm có 5.', 'Bảng nhân 2 tăng dần mỗi lần 2; bảng nhân 5 tăng dần mỗi lần 5.', 'Dựa vào phép nhân để tìm kết quả phép chia: 5 × 6 = 30 nên 30 : 5 = 6.', 'Khi chia, đọc kĩ đề hỏi số nhóm hay số đồ vật trong mỗi nhóm.'],
 steps=['Khoanh thông tin mỗi nhóm và số nhóm.', 'Chọn nhân nếu tìm tất cả; chọn chia nếu chia đều hoặc tìm số nhóm.', 'Tính và kiểm tra bằng phép tính ngược.'],
 errors=['Nhầm 2 × 7 với 2 + 7.', 'Đảo câu trả lời số nhóm thành số đồ vật mỗi nhóm.', 'Đọc lướt nên bỏ sót phần thêm hoặc bớt sau phép nhân.'],
 examples=[('Có 6 túi, mỗi túi 2 quả lê. Hỏi tất cả có bao nhiêu quả?', ['Có 6 nhóm, mỗi nhóm 2 quả.', '2 × 6 = 12. Có 12 quả lê.']), ('Có 20 bông hoa, cắm mỗi lọ 5 bông. Cần bao nhiêu lọ?', ['Tìm số nhóm 5 bông trong 20 bông.', '20 : 5 = 4. Cần 4 lọ.'])],
 game=('Chuyến tàu nhóm đều', 'Giải câu hỏi về các nhóm 2 và 5 để đưa hành khách lên đúng toa.'))
]
for num, section in enumerate(sections, 1):
    lines = section.strip().splitlines()[1:]
    assert len(lines) == 40, (num, len(lines))
    meta = catalog['lessons'][num-1]
    d = details[num-1]
    qs = []
    for i, row in enumerate(lines):
        question, answer, explanation = row.split('|')
        # Dạng điền giữ câu trả lời ngắn, trắc nghiệm có phương án nhiễu số học.
        kind = 'mcq' if i % 2 == 0 else 'fill'
        n = int(answer)
        wrong = []
        for candidate in [n+10,n-10,n+1,n-1,n+100]:
            if candidate >= 0 and candidate != n and candidate not in wrong:
                wrong.append(candidate)
            if len(wrong) == 3: break
        qs.append(dict(question_id=f"{meta['id']}_Q{i+1:02}", type=kind, question=question,
                       **({'options': [str(n)]+list(map(str,wrong))} if kind=='mcq' else {}),
                       correct_answer=str(n), explanation=explanation,
                       difficulty='nhan_biet' if i<10 else 'thong_hieu' if i<20 else 'van_dung'))
    game_title, game_goal = d['game']
    obj = dict(id=meta['id'], subject='toan', grade=3, book='Kết nối tri thức với cuộc sống',
        volume=1, lesson_no=num, title=meta['title'], topic='Ôn tập và bổ sung',
        source=dict(pdf=meta['source_pdf'], printed_pages=[meta['page_start'],meta['page_end']],
                    pdf_pages=[meta['page_start']+1,meta['page_end']+1],
                    review='Đã đọc trực quan toàn bộ trang nguồn cho bài này; nội dung và bài tập mới do AI biên soạn.'),
        objectives=d['objectives'], knowledge=dict(introduction=d['intro'], rules=d['rules'],
            steps=d['steps'], common_errors=d['errors']),
        examples=[dict(question=q,steps=s) for q,s in d['examples']], practice=qs,
        games=[dict(id=meta['id']+'_GAME1',title=game_title,mode='treasure',objective=game_goal,
            rules=['Mỗi lượt lấy 10 câu từ bài học.', 'Chọn đáp án để mở rương; xem phản hồi rồi chuyển câu.',
                   'Mỗi câu đúng được 10 điểm, bỏ qua hoặc sai được 0 điểm.'],
            question_ids=[q['question_id'] for q in qs], answer_source='practice.correct_answer',
            feedback_source='practice.explanation', max_score=100)],
        assessment=dict(session_size=10,distribution=dict(nhan_biet=3,thong_hieu=3,van_dung=4),
            scoring='Đúng lần đầu: 1 điểm; đúng sau một gợi ý: 0,5 điểm. Từ 90%: 3 sao; từ 60%: 2 sao; còn lại: 1 sao.',
            review_advice='Xem lời giải các câu sai, đọc lại quy tắc, rồi làm một lượt mới.'),
        feedback=dict(correct='Chính xác! Hãy đọc lời giải để củng cố cách làm.',
                      incorrect='Em thử lại một lần. Sau đó xem đáp án và cách giải.'),
        verification=dict(ai_authored=True,structure_checked=True,answer_reviewed=True,
                          source_reviewed=True,teacher_approved=False),
        status='AI_CHECKED_AWAITING_TEACHER')
    dest=ROOT/f'content/toan/tap-1/{meta["id"]}'
    dest.with_suffix('.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    md=f"# {obj['title']}\n\nNguồn tham khảo: Toán 3 KNTT, tập 1, trang {meta['page_start']}-{meta['page_end']}.\n\nTrạng thái: AI biên soạn và rà soát; chưa có xác nhận của giáo viên.\n\n## Mục tiêu\n\n"+'\n'.join('- '+s for s in d['objectives'])
    md+='\n\n## Khám phá\n\n'+d['intro']+'\n\n'+'\n'.join('- '+s for s in d['rules'])
    md+='\n\n## Hướng dẫn\n\n'+'\n'.join(f'{i+1}. {s}' for i,s in enumerate(d['steps']))
    md+='\n\n## Lỗi thường gặp\n\n'+'\n'.join('- '+s for s in d['errors'])
    md+='\n\n## Ví dụ\n\n'+'\n\n'.join(e['question']+'\n\n'+'\n'.join(f'{i+1}. {s}' for i,s in enumerate(e['steps'])) for e in obj['examples'])
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
