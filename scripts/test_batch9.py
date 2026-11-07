"""Hồi quy cách đọc khoảng nhiệt kế, chọn đơn vị và nhớ khi nhân."""
import json
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def lesson(n):return json.loads((ROOT/f'content/toan/tap-1/TOAN3_T1_B{n}.json').read_text())
expected={33:{7:'24',8:'32',11:'8',12:'2',27:'20',33:'21',36:'5',38:'3'},34:{11:'35',12:'5',13:'khối lượng',20:'không',29:'3',35:'400',37:'100'},35:{8:'không',12:'300',17:'240',27:'100',28:'4',29:'13',31:'C',40:'144'},36:{7:'2',11:'504',12:'2',15:'0',18:'432',25:'525',29:'86',39:'995',40:'45'}}
seen=set()
for n,cases in expected.items():
 o=lesson(n)
 assert o['status']=='AI_CHECKED_AWAITING_TEACHER' and not o['verification']['teacher_approved']
 for q in o['practice']:
  assert q['question'] not in seen;seen.add(q['question'])
  if 'Hình A' in q['question']:
   assert q['figure']==o['figures'][0]
   ET.parse(ROOT/q['figure']['path'])
 for ordinal,answer in cases.items():assert o['practice'][ordinal-1]['correct_answer']==answer,(n,ordinal)
assert len(seen)==160
# Mọi câu dạng Tính/Nhẩm nhân thuần túy được tính lại từ hai thừa số.
import re
for q in lesson(36)['practice']:
 m=re.fullmatch(r'Tính(?: nhẩm)? (\d+) × (\d+)\.',q['question'])
 if m:assert int(q['correct_answer'])==int(m[1])*int(m[2])
assert int(lesson(33)['practice'][10]['correct_answer'])==32-24
assert int(lesson(34)['practice'][10]['correct_answer'])==35-0
assert int(lesson(35)['practice'][26]['correct_answer'])==600-250*2
assert int(lesson(36)['practice'][10]['correct_answer'])==126*4
assert int(lesson(36)['practice'][11]['correct_answer'])==(207*3//10)%10
assert int(lesson(36)['practice'][38]['correct_answer'])==265*3+200
print('PASS Batch 9: 160 câu không trùng, 32 đáp án trọng yếu, đọc vạch và số nhớ nhân.')
