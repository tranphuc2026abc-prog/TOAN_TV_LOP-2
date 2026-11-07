"""Hình mới cho mô hình khối, trung điểm, đường tròn và sơ đồ gấp số lần."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'content/toan/tap-1'
def save(name,title,desc,body,height=320):
    (ROOT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 {height}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc><rect width="560" height="{height}" rx="18" fill="#f4f7ff"/><g font-family="sans-serif" font-size="22" fill="#17345e">{body}</g></svg>\n')
def block(name,title,points):
    p=points;body=f'<text x="20" y="30">{title}</text>'
    hidden=['EH','HG','DH']
    for edge in ['AB','BC','CD','DA','EF','FG','GH','HE','AE','BF','CG','DH']:
        a,b=p[edge[0]],p[edge[1]]
        dash=' stroke-dasharray="7 5"' if edge in hidden or edge[::-1] in hidden else ''
        body+=f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" fill="none" stroke="#28609b" stroke-width="3"{dash}/>'
    for label,(x,y) in p.items():
        dx,dy=(-20,5) if label in ['D','H'] else (8,23) if label in ['C','G'] else (-8,-12)
        body+=f'<circle cx="{x}" cy="{y}" r="4"/><text x="{x+dx}" y="{y+dy}">{label}</text>'
    body+='<text x="35" y="298" font-size="17">Nét đứt: cạnh khuất. Hình biểu diễn không dùng để đo.</text>'
    save(name,title,'Mô hình có tám đỉnh A, B, C, D, E, F, G, H. Cạnh khuất vẽ nét đứt; cần tính đủ phần phía sau.',body)
block('TOAN3_T1_B21_A.svg','Hình A: Khối lập phương',dict(A=(100,115),B=(220,115),C=(220,235),D=(100,235),E=(160,65),F=(280,65),G=(280,185),H=(160,185)))
block('TOAN3_T1_B21_B.svg','Hình B: Khối hộp chữ nhật',dict(A=(80,125),B=(290,125),C=(290,225),D=(80,225),E=(140,65),F=(350,65),G=(350,165),H=(140,165)))
body='<text x="20" y="30">Hình A</text><path d="M180 60H380V260H180Z" fill="#e9f5ff" stroke="#17345e" stroke-width="3"/>'
for x,y,label,dx,dy in [(180,60,'A',-24,-10),(380,60,'B',8,-10),(380,260,'C',8,28),(180,260,'D',-24,28),(280,60,'M',-8,-10),(380,160,'N',12,7),(280,260,'P',-8,28),(180,160,'Q',-27,7)]:
    color='#e09a31' if label in 'MNPQ' else '#17345e'
    body+=f'<circle cx="{x}" cy="{y}" r="5" fill="{color}"/><text x="{x+dx}" y="{y+dy}">{label}</text>'
save('TOAN3_T1_B22_A.svg','Hình A: Đánh dấu trên bốn cạnh hình vuông','Hình vuông ABCD, các điểm M, N, P, Q ở trung điểm các cạnh AB, BC, CD, DA.',body)
body='<text x="20" y="30">Hình B</text><rect x="180" y="60" width="200" height="200" fill="#fff1dc" stroke="#17345e" stroke-width="3"/><circle cx="280" cy="160" r="100" fill="#d6f0e6" stroke="#25875d" stroke-width="3"/><path d="M280 160H380" stroke="#28609b" stroke-width="3"/><circle cx="280" cy="160" r="4"/><text x="285" y="187">O</text>'
save('TOAN3_T1_B22_B.svg','Hình B: Đường tròn vừa khít hình vuông','Đường tròn tâm O nằm trong hình vuông và vừa chạm cả bốn cạnh. Cạnh hình vuông bằng đường kính đường tròn.',body)
body='<text x="20" y="30">Hình A: Sơ đồ số thẻ</text><text x="20" y="110">Bình</text><text x="20" y="200">Lan</text><rect x="120" y="80" width="100" height="45" fill="#d9eaff" stroke="#17345e" stroke-width="2"/>'
for part in range(3):
    body+=f'<rect x="{120+100*part}" y="170" width="100" height="45" fill="{"#d6f0e6" if part%2==0 else "#ecf9f3"}" stroke="#17345e" stroke-width="2"/>'
    for k in range(5):body+=f'<circle cx="{130+100*part+16*k}" cy="192" r="4"/>'
for k in range(5):body+=f'<circle cx="{130+16*k}" cy="102" r="4"/>'
body+='<text x="140" y="150" font-size="18">1 phần: 5 thẻ</text><text x="145" y="250" font-size="19">3 phần bằng nhau, mỗi phần 5 thẻ</text>'
save('TOAN3_T1_B24_A.svg','Hình A: Số thẻ Lan gấp ba lần Bình','Bình có một phần gồm năm thẻ. Lan có ba phần bằng nhau, mỗi phần bằng số thẻ Bình.',body,290)
print('Đã dựng 5 SVG cho Batch 6.')
