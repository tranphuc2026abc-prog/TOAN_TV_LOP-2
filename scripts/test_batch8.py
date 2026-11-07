"""Hồi quy Batch 8: đơn vị, phép đo không ở 0, cân cả bì và nước tràn."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def lesson(n): return json.loads((ROOT/f'content/toan/tap-1/TOAN3_T1_B{n}.json').read_text())
expected={29:{21:'2',23:'11',24:'12',26:'63',40:'44'},30:{3:'1000',9:'26',10:'4',12:'27',18:'4',26:'640',34:'30',36:'115'},31:{6:'350',12:'250',14:'trái',18:'200',25:'100',27:'120',35:'180'},32:{6:'300',12:'200',14:'có',22:'375',26:'50',36:'630',39:'4'}}
seen=set()
for n,cases in expected.items():
 obj=lesson(n)
 assert obj['status']=='AI_CHECKED_AWAITING_TEACHER' and not obj['verification']['teacher_approved']
 for q in obj['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
 for ordinal,value in cases.items():assert obj['practice'][ordinal-1]['correct_answer']==value,(n,ordinal)
 if n>29:
  assert obj['activities']
  for q in obj['practice']:
   if 'Hình A' in q['question']:
    assert q['figure']==obj['figures'][0]
    svg=ET.parse(ROOT/q['figure']['path']).getroot()
    assert svg.attrib['viewBox']=='0 0 560 300'
    assert svg.find('{http://www.w3.org/2000/svg}title') is not None
assert len(seen)==160
# Tính độc lập các tình huống tiêu biểu thay vì chỉ kiểm tra văn bản đáp án.
assert int(lesson(30)['practice'][8]['correct_answer'])==30-4
assert int(lesson(31)['practice'][5]['correct_answer'])==200+100+50
assert int(lesson(31)['practice'][26]['correct_answer'])==(450-90)//3
assert int(lesson(32)['practice'][25]['correct_answer'])==650+400-1000
assert int(lesson(29)['practice'][22]['correct_answer'])==57//5
assert int(lesson(29)['practice'][23]['correct_answer'])==(57+5-1)//5
print('PASS Batch 8: 160 câu không trùng, 27 đáp án trọng yếu, hình/đơn vị và tình huống đo lường.')
