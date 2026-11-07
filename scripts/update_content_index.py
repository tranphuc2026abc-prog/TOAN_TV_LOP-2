"""Đồng bộ chỉ mục và xác nhận thẩm định, không tự cấp duyệt cho bài mới."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
catalog=json.loads((ROOT/'data/CHUONG_TRINH_LOP_3_FULL.json').read_text())
approvals=json.loads((ROOT/'content/system/APPROVALS.json').read_text())
approved={id:confirmation for confirmation in approvals['confirmations'] for id in confirmation['lesson_ids']}
entries=[]
for meta in catalog['lessons']:
    candidates=list((ROOT/'content').glob(f'*/tap-*/{meta["id"]}.json'))
    assert len(candidates)<=1, meta['id']
    obj=json.loads(candidates[0].read_text()) if candidates else None
    is_approved=meta['id'] in approved
    if obj:
        obj['verification']['teacher_approved']=is_approved
        obj['status']='TEACHER_APPROVED' if is_approved else 'AI_CHECKED_AWAITING_TEACHER'
        if is_approved: obj['verification']['teacher_confirmation']=approved[meta['id']]
        candidates[0].write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
        md=candidates[0].with_suffix('.md')
        if is_approved:
            md.write_text(md.read_text().replace('Trạng thái: AI biên soạn và rà soát; chưa có xác nhận của giáo viên.', 'Trạng thái: Giáo viên Nguyễn Thế Khanh đã xem và thẩm định Batch 1 (07/11/2026).'))
    entries.append(dict(id=meta['id'],subject=meta['subject'],volume=meta['volume'],title=meta['title'],
        path=str(candidates[0].relative_to(ROOT)) if obj else None,
        markdown=str(candidates[0].with_suffix('.md').relative_to(ROOT)) if obj else None,
        question_count=len(obj['practice']) if obj else None,game_count=len(obj['games']) if obj else None,
        status='DA_HOAN_THIEN' if is_approved else 'CAN_RA_SOAT' if obj else 'BAN_NHAP',
        note='Giáo viên đã thẩm định.' if is_approved else 'AI đã rà soát nguồn, đáp án; chờ giáo viên thẩm định.' if obj else 'Có bài mẫu hoặc bản nháp tự động; chưa kiểm định từng bài.'))
out=dict(updated='2026-11-07',total=len(entries),counts=catalog['counts'],lessons=entries)
(ROOT/'content/system/INDEX.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Chỉ mục:',len(entries),'mục;',sum(e['path'] is not None for e in entries),'có học liệu riêng;',len(approved),'đã thẩm định.')
