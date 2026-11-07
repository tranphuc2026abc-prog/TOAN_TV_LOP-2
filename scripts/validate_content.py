"""Kiểm tra toàn bộ học liệu, tham chiếu hình/trò chơi và đồng bộ Markdown."""
import json, re, ast, operator
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
index=json.loads((ROOT/'content/system/INDEX.json').read_text())
ids=set();total=0;ready=0;equations=0
ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def calculate(node):
    if isinstance(node,ast.Constant) and type(node.value) is int: return node.value
    if isinstance(node,ast.BinOp) and type(node.op) in ops:
        return ops[type(node.op)](calculate(node.left),calculate(node.right))
    raise ValueError('Chỉ cho phép phép tính số học nguyên trong lời giải.')
assert len(index['lessons'])==index['total']==168
assert len({e['id'] for e in index['lessons']})==168
for entry in index['lessons']:
    if not entry['path']: continue
    obj=json.loads((ROOT/entry['path']).read_text());ready+=1
    assert obj['id']==entry['id'] and len(obj['practice'])==entry['question_count']==40
    assert len(obj['games'])==entry['game_count']
    md=(ROOT/entry['markdown']).read_text();counts={};prompts=set()
    for q in obj['practice']:
        assert q['question_id'] not in ids;ids.add(q['question_id'])
        assert q['question'] not in prompts;prompts.add(q['question'])
        assert q['correct_answer'] is not None and q['explanation']
        assert q['question'] in md and q['explanation'] in md
        for match in re.finditer(r'(\d+(?:(?:\s*[+×\-]\s*| : )\d+)+)\s*=\s*(\d+(?:(?:\s*[+×\-]\s*| : )\d+)*)',q['explanation']):
            expr=match[1].replace('×','*').replace(':','/')
            rhs=match[2].replace('×','*').replace(':','/')
            assert calculate(ast.parse(expr,mode='eval').body)==calculate(ast.parse(rhs,mode='eval').body), (q['question_id'],match[0])
            equations+=1
        counts[q['difficulty']]=counts.get(q['difficulty'],0)+1
        if q['type']=='mcq':
            assert len(q['options'])==len(set(q['options']))==4 and q['correct_answer'] in q['options']
        if q.get('figure'): assert (ROOT/q['figure']['path']).exists()
    assert counts==dict(nhan_biet=10,thong_hieu=10,van_dung=20)
    for game in obj['games']:
        assert set(game['question_ids'])=={q['question_id'] for q in obj['practice']}
        assert game['mode'] in ['match','speed','treasure','tf'] and game['rules']
    assert (entry['status']=='DA_HOAN_THIEN')==obj['verification']['teacher_approved']
    total+=len(obj['practice'])
print(f'PASS: {ready} bài, {total} câu; phân mức 10/10/20; ID, đáp án, lựa chọn, lời giải, Markdown, hình và trạng thái đồng bộ.')
print(f'Đã tính lại {equations} đẳng thức số trong lời giải; không thay thế thẩm định ngữ nghĩa của giáo viên.')
