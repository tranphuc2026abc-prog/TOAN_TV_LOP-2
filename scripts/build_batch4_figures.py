"""Dựng hình chính xác bằng SVG; không sao chép hình sách giáo khoa."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'content/toan/tap-1'
def svg(name,title,description,body,height=230):
    markup=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{description}</desc>
<rect width="560" height="{height}" rx="18" fill="#f3f7ff"/>
<g font-family="sans-serif" fill="#17345e">{body}</g></svg>'''
    (ROOT/name).write_text(markup+'\n')

body='<text x="20" y="30" font-size="22">Hình A: bốn dải bằng nhau</text>'
for col in range(4):
    body+=f'<rect x="{80+col*100}" y="65" width="100" height="100" fill="{"#42a5e6" if col==0 else "white"}" stroke="#17345e" stroke-width="2"/>'
body+='<text x="90" y="205" font-size="18">Tô một dải trong bốn dải bằng nhau.</text>'
svg('TOAN3_T1_B14_A.svg','Hình A — Một phần tư','Một hình chữ nhật chia thành bốn dải có cùng chiều rộng, tô xanh dải thứ nhất.',body)
body='<text x="20" y="30" font-size="22">Hình B: sáu ô bằng nhau</text>'
for row in range(2):
    for col in range(3):
        body+=f'<rect x="{130+col*100}" y="{55+row*65}" width="100" height="65" fill="{"#f5b64d" if row==0 and col==0 else "white"}" stroke="#17345e" stroke-width="2"/>'
body+='<text x="90" y="215" font-size="18">Tô một ô trong sáu ô bằng nhau.</text>'
svg('TOAN3_T1_B14_B.svg','Hình B — Một phần sáu','Một hình chữ nhật có hai hàng và ba cột tạo sáu ô bằng nhau, tô vàng ô đầu tiên.',body)

body='''<text x="20" y="30" font-size="22">Hình C: A, M, B thẳng hàng</text>
<path d="M80 115H480" stroke="#17345e" stroke-width="3"/>
<text x="160" y="92" font-size="22">4 cm</text><text x="360" y="92" font-size="22">4 cm</text>'''
for x,label in [(80,'A'),(280,'M'),(480,'B')]:
    body+=f'<circle cx="{x}" cy="115" r="6"/><text x="{x-9}" y="150" font-size="24">{label}</text>'
body+='<text x="85" y="205" font-size="18">AM = MB = 4 cm; M nằm giữa A và B.</text>'
svg('TOAN3_T1_B16_C.svg','Hình C — Trung điểm M','A, M, B thẳng hàng theo thứ tự đó. AM dài 4 cm, MB dài 4 cm.',body)
body='''<text x="20" y="30" font-size="22">Hình D: C, N, D thẳng hàng</text>
<path d="M80 115H480" stroke="#17345e" stroke-width="3"/>
<text x="103" y="92" font-size="22">2 cm</text><text x="305" y="92" font-size="22">6 cm</text>'''
for x,label in [(80,'C'),(180,'N'),(480,'D')]:
    body+=f'<circle cx="{x}" cy="115" r="6"/><text x="{x-9}" y="150" font-size="24">{label}</text>'
body+='<text x="90" y="205" font-size="18">N ở giữa, nhưng CN khác ND.</text>'
svg('TOAN3_T1_B16_D.svg','Hình D — Điểm ở giữa chưa là trung điểm','C, N, D thẳng hàng theo thứ tự đó. CN dài 2 cm, ND dài 6 cm.',body)
body='''<text x="20" y="30" font-size="22">Hình E: R không nằm trên PQ</text>
<path d="M100 180H460M100 180L280 65L460 180" fill="none" stroke="#17345e" stroke-width="3"/>
<text x="70" y="210" font-size="24">P</text><text x="468" y="210" font-size="24">Q</text><text x="272" y="53" font-size="24">R</text>
<circle cx="100" cy="180" r="6"/><circle cx="460" cy="180" r="6"/><circle cx="280" cy="65" r="6"/>
<text x="205" y="238" font-size="18">RP = RQ</text>'''
svg('TOAN3_T1_B16_E.svg','Hình E — Hai khoảng cách bằng nhau chưa đủ','P và Q ở trên đường thẳng ngang; R nằm phía trên, ngoài đoạn PQ. RP bằng RQ.',body,260)
print('Đã dựng 5 hình SVG cho Bài 14 và 16.')
