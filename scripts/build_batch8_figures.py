"""Hình SVG tự dựng, dữ kiện tỉ lệ chính xác cho Batch 8."""
from pathlib import Path
from xml.sax.saxutils import escape
ROOT=Path(__file__).resolve().parents[1]/'content/toan/tap-1'
def save(n,title,body):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 300" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(title)}</desc><rect width="560" height="300" rx="16" fill="#f6faff"/><g font-family="sans-serif" font-size="18" fill="#17345e">{body}</g></svg>\n'
 (ROOT/f'TOAN3_T1_B{n}_A.svg').write_text(svg)
# 10 px cho mỗi mm. Các nhãn cm nằm dưới, vạch mm phụ cách đều.
b='<text x="30" y="35">Hình A — thước chia từng mm</text><rect x="50" y="145" width="430" height="75" rx="8" fill="#fff2bf" stroke="#b09335"/>'
for i in range(41):
 x=65+i*10; h=25 if i%10==0 else 18 if i%5==0 else 11
 b+=f'<path d="M{x} 150v{h}" stroke="#17345e" stroke-width="1.5"/>'
 if i%10==0:b+=f'<text x="{x}" y="205" text-anchor="middle">{i//10}</text>'
b+='<text x="485" y="205">cm</text><path d="M105 115H365M105 110V150M365 110V150" stroke="#237b5a" stroke-width="4"/><circle cx="105" cy="115" r="5" fill="#237b5a"/><circle cx="365" cy="115" r="5" fill="#237b5a"/><text x="105" y="96" text-anchor="middle">A</text><text x="365" y="96" text-anchor="middle">B</text><text x="280" y="260" text-anchor="middle" font-size="15">Hình mô phỏng; không dùng thước thật đo màn hình.</text>'
save(30,'Thước 0 đến 4 cm; A ở 4 mm, B ở 30 mm.',b)
b='<text x="25" y="35">Hình A — cân đã thăng bằng</text><path d="M280 115L235 260H325Z" fill="#98cbe6" stroke="#17345e"/><path d="M90 110H470" stroke="#17345e" stroke-width="7"/><circle cx="280" cy="110" r="12" fill="#f3be51" stroke="#17345e"/>'
for x in [135,425]:
 b+=f'<path d="M{x-65} 210L{x} 110L{x+65} 210Z" fill="none" stroke="#456781" stroke-width="2"/><path d="M{x-70} 210Q{x} 255 {x+70} 210Z" fill="#b7e2f5" stroke="#17345e"/>'
b+='<path d="M105 150Q135 135 165 150L175 205H95Z" fill="#a6d9af" stroke="#237b5a"/><text x="135" y="183" text-anchor="middle" font-size="16">Túi hạt</text>'
for x,w,label,y in [(370,42,'200 g',158),(418,42,'100 g',171),(466,34,'50 g',184)]:
 b+=f'<rect x="{x-18}" y="{y}" width="{w}" height="{210-y}" rx="4" fill="#aebbc8" stroke="#17345e"/><text x="{x+3}" y="{y-8}" text-anchor="middle" font-size="14">{label}</text>'
b+='<text x="280" y="285" text-anchor="middle" font-size="16">Hai đĩa ngang nhau: khối lượng hai bên bằng nhau.</text>'
save(31,'Cân thăng bằng: túi hạt đối diện ba quả cân 200 g, 100 g và 50 g.',b)
b='<text x="25" y="35">Hình A — ca chia vạch ml</text><path d="M340 85H375Q410 160 375 225H340" fill="none" stroke="#4f718c" stroke-width="9"/><rect x="170" y="130" width="170" height="110" fill="#9ad8ed"/><path d="M170 55V240H340V55" fill="none" stroke="#17345e" stroke-width="3"/><path d="M170 130H340" stroke="#227ba0" stroke-width="3"/>'
for v in range(0,501,100):
 y=240-v*.36
 b+=f'<path d="M170 {y}H192" stroke="#17345e" stroke-width="2"/><text x="205" y="{y+6}">{v}</text>'
b+='<text x="290" y="80">ml</text><text x="280" y="280" text-anchor="middle" font-size="16">Ca tối đa 500 ml; mỗi khoảng là 100 ml.</text>'
save(32,'Ca chia vạch 0 đến 500 ml, mỗi vạch 100 ml; mực nước tại 300 ml.',b)
print('Đã dựng 3 SVG: thước, cân, ca.')
