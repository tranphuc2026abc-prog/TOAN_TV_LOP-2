"""Dựng mới thang nhiệt kế và thước đúng vạch cho Batch 9."""
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]/'content/toan/tap-1'
def save(n,title,body):
 (ROOT/f'TOAN3_T1_B{n}_A.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 360" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(title)}</desc><rect width="560" height="360" rx="16" fill="#f6faff"/><g font-family="sans-serif" font-size="18" fill="#17345e">{body}</g></svg>\n')
b='<text x="25" y="32">Hình A — mỗi khoảng nhỏ: 2 °C</text>'
for x,name,value in [(145,'P',24),(385,'Q',32)]:
 b+=f'<text x="{x}" y="64" text-anchor="middle">{name}</text><rect x="{x-22}" y="78" width="44" height="225" rx="18" fill="white" stroke="#52758f" stroke-width="2"/><circle cx="{x}" cy="300" r="24" fill="#d7524b" stroke="#52758f" stroke-width="2"/><rect x="{x-7}" y="{280-value*5}" width="14" height="{value*5+22}" fill="#d7524b"/><text x="{x+65}" y="60">°C</text>'
 for v in range(0,41,2):
  y=280-v*5;end=x+45 if v%10==0 else x+35
  b+=f'<path d="M{x+24} {y}H{end}" stroke="#17345e"/>'
  if v%10==0:b+=f'<text x="{x+52}" y="{y+6}">{v}</text>'
b+='<text x="280" y="345" text-anchor="middle" font-size="15">Dữ liệu mô phỏng để đọc thang đo, không phải dự báo thời tiết.</text>'
save(33,'Hai nhiệt kế: P tại 24 độ C; Q tại 32 độ C; mỗi khoảng nhỏ 2 độ C.',b)
b='<text x="25" y="38">Hình A — thẻ đặt từ vạch 0</text><rect x="60" y="185" width="430" height="85" rx="7" fill="#fff2bf" stroke="#b09335"/>'
for i in range(41):
 x=75+i*10;h=27 if i%10==0 else 18 if i%5==0 else 10
 b+=f'<path d="M{x} 190v{h}" stroke="#17345e"/>'
 if i%10==0:b+=f'<text x="{x}" y="250" text-anchor="middle">{i}</text>'
b+='<text x="500" y="250">mm</text><rect x="75" y="100" width="350" height="65" rx="4" fill="#a9d9ef" stroke="#28759b" stroke-width="2"/><path d="M75 165V190M425 165V190" stroke="#28759b" stroke-dasharray="4 3"/><text x="250" y="140" text-anchor="middle">Thẻ</text><text x="280" y="325" text-anchor="middle" font-size="15">Mỗi khoảng nhỏ là 1 mm; hình không có kích thước thật.</text>'
save(34,'Thước chia mỗi mm từ 0 đến 40; thẻ từ 0 đến 35 mm.',b)
print('Đã dựng 2 SVG Batch 9.')
