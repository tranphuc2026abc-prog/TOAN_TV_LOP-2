"""Hồi quy các khác biệt ngữ nghĩa dễ nhầm của Batch 7."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
def lesson(n): return json.loads((root/f'content/toan/tap-1/TOAN3_T1_B{n}.json').read_text())
expected={25:{21:'6',22:'7',25:'5',26:'5',37:'không',38:'27'},26:{11:'24',23:'13',30:'1',38:'1',40:'không'},27:{21:'8',22:'24',35:'48',38:'45'},28:{11:'30',17:'31',32:'42',34:'63',39:'24'}}
for n,cases in expected.items():
    obj=lesson(n)
    assert obj['status']=='AI_CHECKED_AWAITING_TEACHER'
    assert not obj['verification']['teacher_approved']
    for ordinal,answer in cases.items():
        assert obj['practice'][ordinal-1]['correct_answer']==answer,(n,ordinal)
# Hai cách đặt câu hỏi cùng dữ kiện phải có hai cách xử lí số dư.
a,b=lesson(25)['practice'][20:22]
assert 'đầy' in a['question'] and 'chứa hết' in b['question']
assert int(a['correct_answer'])==25//4
assert int(b['correct_answer'])==(25+4-1)//4
# Giảm số còn lại khác với lượng đã chuyển đi.
a,b=lesson(27)['practice'][20:22]
assert int(a['correct_answer'])==32//4
assert int(b['correct_answer'])==32-32//4
print('PASS Batch 7: số dư/chứa hết, hạ chục dư, giảm số lần, lượng dùng/còn và hai bước.')
