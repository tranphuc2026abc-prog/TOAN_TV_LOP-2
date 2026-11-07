"""Hình học SVG mới cho Bài 17–20, dùng tọa độ để giữ đúng tính chất."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'content/toan/tap-1'
def save(name,title,desc,body,height=320,width=560):
    (ROOT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc><rect width="{width}" height="{height}" rx="18" fill="#f4f7ff"/><g font-family="sans-serif" font-size="22" fill="#17345e">{body}</g></svg>\n')
def point(x,y,label,dx=-8,dy=29):
    return f'<circle cx="{x}" cy="{y}" r="4"/><text x="{x+dx}" y="{y+dy}">{label}</text>'
body='''<text x="20" y="30">Hình A</text><circle cx="280" cy="170" r="100" fill="#e4f7f1" stroke="#17345e" stroke-width="3"/>
<path d="M180 170H380M280 170V70M200 110H360" fill="none" stroke="#245994" stroke-width="3"/>'''
for x,y,label,dx,dy in [(280,170,'O',6,28),(180,170,'A',-24,5),(380,170,'B',10,5),(280,70,'C',-8,-13),(200,110,'D',-24,-9),(360,110,'E',9,-9)]: body+=point(x,y,label,dx,dy)
save('TOAN3_T1_B17_A.svg','Hình A: Hình tròn tâm O','AB qua tâm O; C, D, E trên đường tròn. OC nối tâm tới C; đoạn DE không qua O.',body)

body='<text x="20" y="30">Hình A</text>'
angles=[('I',[(65,175,'O'),(65,75,'A'),(165,175,'B')]),('II',[(250,175,'P'),(300,75,'M'),(350,175,'N')]),('III',[(445,175,'E'),(375,105,'C'),(555,175,'D')])]
for title,pts in angles:
    v,a,b=pts
    body+=f'<text x="{v[0]+20}" y="245">{title}</text><path d="M{a[0]} {a[1]}L{v[0]} {v[1]}L{b[0]} {b[1]}" stroke="#17345e" stroke-width="3" fill="none"/>'
    for x,y,label in pts: body+=point(x,y,label,-8,-12 if label in ['A','M','C'] else 29)
save('TOAN3_T1_B18_A.svg','Hình A: Ba góc ở các đỉnh O, P, E','Góc I có cạnh OA thẳng đứng và OB nằm ngang. Góc II có PM chếch lên và PN nằm ngang. Góc III có EC chếch lên trái và ED nằm ngang.',body,280,600)
body='<text x="20" y="30">Hình B</text><path d="M200 90L280 170L360 90" stroke="#17345e" stroke-width="3" fill="none"/>'
for x,y,label in [(200,90,'L'),(280,170,'K'),(360,90,'M')]: body+=point(x,y,label,-8,-13 if label!='K' else 30)
save('TOAN3_T1_B18_B.svg','Hình B: Góc có đỉnh K','Hai cạnh KL và KM tạo góc vuông được xoay nghiêng so với mép hình.',body,240)

body='<text x="20" y="30">Hình A</text><path d="M85 65L35 185L135 185ZM210 100H350V180H210ZM410 95H500V185H410Z" fill="#e9f4ff" stroke="#17345e" stroke-width="3"/>'
for x,y,label,dx,dy in [(85,65,'A',-8,-12),(35,185,'B',-18,27),(135,185,'C',5,27),(210,100,'D',-20,-12),(350,100,'E',8,-12),(350,180,'F',8,28),(210,180,'G',-20,28),(410,95,'M',-18,-12),(500,95,'N',7,-12),(500,185,'P',7,28),(410,185,'Q',-18,28)]: body+=point(x,y,label,dx,dy)
save('TOAN3_T1_B19_A.svg','Hình A: Tam giác ABC, chữ nhật DEFG và vuông MNPQ','Ba hình tách rời. Các tên đỉnh đi theo thứ tự quanh mỗi hình. Hình minh họa không thay cho thước đo độ dài thật.',body,245)
body='<text x="20" y="30">Hình B</text><path d="M80 165L280 65L480 165L280 265Z" fill="#fff2d8" stroke="#17345e" stroke-width="3"/>'
for x,y,label,dx,dy in [(80,165,'R',-25,5),(280,65,'S',-8,-12),(480,165,'T',10,5),(280,265,'U',-8,30)]: body+=point(x,y,label,dx,dy)
save('TOAN3_T1_B19_B.svg','Hình B: Tứ giác RSTU','Tứ giác có bốn cạnh bằng nhau nhưng các góc không vuông.',body)

body='<text x="20" y="30">Hình A — Mỗi khoảng lưới là một ô</text>'
for origin in [40,320]:
    for n in range(6):
        x=origin+40*n;y=55+40*n
        body+=f'<path d="M{x} 55V255M{origin} {y}H{origin+200}" stroke="#bccde1" stroke-width="1"/>'
body+='<path d="M40 95H200V175H40ZM360 95H480V215H360Z" fill="none" stroke="#17345e" stroke-width="3"/><text x="20" y="290" font-size="19">Chữ nhật: dài 4 ô, rộng 2 ô</text><text x="315" y="290" font-size="19">Hình vuông: cạnh 3 ô</text>'
save('TOAN3_T1_B20_A.svg','Hình A: Vẽ chữ nhật và hình vuông trên lưới','Bên trái hình chữ nhật dài bốn khoảng ô, rộng hai khoảng ô. Bên phải hình vuông có cạnh ba khoảng ô. Một ô màn hình không được xem là một cm thật.',body)
print('Đã dựng 6 SVG cho Bài 17–20.')
