# -*- coding: utf-8 -*-
"""رسومات SVG بهوية الموقع (أزرق/برتقالي) — رسومات توضيحية مش صور شغل حقيقي."""
import os, math, random
P="#0b5cad"; PD="#083f78"; A="#f59e0b"; BG="#f5f8fc"; LINE="#dbe4f0"; W="#ffffff"
GROUT="#c9d6e6"

def svg(w,h,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>'

def lerp(a,b,t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
def poly(pts,fill,stroke=None,sw=0,extra=""):
    s=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    st=f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else ""
    return f'<polygon points="{s}" fill="{fill}"{st} {extra}/>'

# ── الصورة الرئيسية: أرضية بمنظور، نصها متبلط، وميزان وكرتون بلاط ──
def hero():
    w,h=800,560
    b=[f'<rect width="{w}" height="{h}" fill="{BG}"/>']
    # الحائط
    b.append(f'<rect x="0" y="0" width="{w}" height="250" fill="#e8eef6"/>')
    # نعلة
    b.append(f'<rect x="0" y="238" width="{w}" height="14" fill="{W}" stroke="{LINE}"/>')
    # أرضية بمنظور
    tl,tr,br,bl=(120,252),(680,252),(w+140,h),(-140,h)
    b.append(poly([tl,tr,br,bl],"#d9cbb2"))  # أسمنت/لياسة
    n=8; m=6
    def pt(i,j):
        L=lerp(tl,bl,j/m); R=lerp(tr,br,j/m)
        # تصحيح منظور بسيط للصفوف
        return lerp(L,R,i/n)
    random.seed(4)
    for j in range(m):
        for i in range(n):
            laid = (i+j*0.9) < 9.5
            if not laid: continue
            q=[pt(i,j),pt(i+1,j),pt(i+1,j+1),pt(i,j+1)]
            # فاصل: تصغير البلاطة نحو مركزها
            cx=sum(p[0] for p in q)/4; cy=sum(p[1] for p in q)/4
            g=0.94
            q2=[(cx+(x-cx)*g, cy+(y-cy)*g) for x,y in q]
            shade = ["#ffffff","#f7f9fc","#eef3f9"][(i+j)%3]
            b.append(poly(q2,shade,GROUT,1))
    # خط الخيط
    b.append(f'<line x1="{pt(0,3)[0]:.0f}" y1="{pt(0,3)[1]:.0f}" x2="{pt(8,3)[0]:.0f}" y2="{pt(8,3)[1]:.0f}" stroke="{A}" stroke-width="2" stroke-dasharray="8 6"/>')
    # كرتون بلاط
    b.append(f'<g transform="translate(560,330)"><rect width="150" height="70" rx="6" fill="{PD}"/><rect y="-18" width="150" height="22" rx="4" fill="{P}"/><text x="75" y="45" text-anchor="middle" font-family="Tajawal,Arial" font-weight="700" font-size="20" fill="{W}">60×120</text></g>')
    # ميزان ماء
    b.append(f'<g transform="translate(250,410) rotate(-4)"><rect width="260" height="34" rx="6" fill="{A}"/><rect x="110" y="8" width="40" height="18" rx="9" fill="#fff7e0" stroke="{PD}" stroke-width="2"/><circle cx="130" cy="17" r="5" fill="#7cc576"/><rect x="18" y="12" width="6" height="10" rx="2" fill="{PD}"/><rect x="236" y="12" width="6" height="10" rx="2" fill="{PD}"/></g>')
    # مسطرين/مشط
    b.append(f'<g transform="translate(90,450) rotate(12)"><path d="M0 0h110l-10 34H10z" fill="#9fb3c8"/><path d="M10 34l6 8 6-8 6 8 6-8 6 8 6-8 6 8 6-8 6 8 6-8 6 8 6-8" fill="none" stroke="#9fb3c8" stroke-width="3"/><rect x="40" y="-34" width="30" height="36" rx="6" fill="{PD}"/></g>')
    # صلبان فواصل
    for x,y in [(470,380),(500,470),(700,470)]:
        b.append(f'<g transform="translate({x},{y})" fill="{P}"><rect x="-10" y="-2.5" width="20" height="5" rx="1"/><rect x="-2.5" y="-10" width="5" height="20" rx="1"/></g>')
    return svg(w,h,"".join(b),"رسم توضيحي لأرضية يتم تبليطها بالميزان")

# ── رسومات الخدمات 320×200 ──
def frame(body,title):
    return svg(320,200,f'<rect width="320" height="200" rx="0" fill="{BG}"/>'+body,title)

def grid_tiles(x0,y0,cols,rows,tw,th,gap,fills,stroke=GROUT,offset=False):
    out=[]
    for r in range(rows):
        off = (tw+gap)/2 if (offset and r%2) else 0
        for c in range(-1 if offset else 0, cols):
            x=x0+c*(tw+gap)+off; y=y0+r*(th+gap)
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{tw}" height="{th}" fill="{fills[(r+c)%len(fills)]}" stroke="{stroke}" stroke-width="1"/>')
    return "".join(out)

def clip(body,x,y,w,h,idn):
    return f'<defs><clipPath id="{idn}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/></clipPath></defs><g clip-path="url(#{idn})">{body}</g>'

def s_ceramic():
    t=grid_tiles(20,20,6,4,44,38,4,[W,"#eef3f9"])
    return frame(clip(f'<rect x="20" y="20" width="280" height="160" fill="{GROUT}"/>'+t,20,20,280,160,"c1"),"بلاط سيراميك 60×60")

def s_porcelain():
    t=grid_tiles(20,20,3,3,92,50,3,["#ffffff","#f3f6fa","#e9eff7"])
    clips="".join(f'<rect x="{20+c*95-6:.0f}" y="{20+r*53-6:.0f}" width="12" height="12" rx="2" fill="{A}"/>' for r in range(1,3) for c in range(1,3))
    return frame(clip(f'<rect x="20" y="20" width="280" height="160" fill="{GROUT}"/>'+t+clips,20,20,280,160,"c2"),"بورسلين مقاسات كبيرة مع كليبسات تسوية")

def s_marble():
    veins=[]
    random.seed(7)
    for k in range(7):
        x=random.randint(10,300); y=20
        d=f"M{x} {y}"
        for s in range(6):
            x+=random.randint(-30,30); y+=28
            d+=f" Q{x+random.randint(-20,20)} {y-14} {x} {y}"
        veins.append(f'<path d="{d}" fill="none" stroke="#b9c4d2" stroke-width="{random.choice([1,1.5,2.5])}" opacity=".8"/>')
    body=f'<rect x="20" y="20" width="280" height="160" fill="#fbfcfd"/>'+"".join(veins)+f'<line x1="160" y1="20" x2="160" y2="180" stroke="{GROUT}" stroke-width="2"/><line x1="20" y1="100" x2="300" y2="100" stroke="{GROUT}" stroke-width="2"/>'
    return frame(clip(body,20,20,280,160,"c3"),"رخام بعروق طبيعية")

def s_bath():
    wall=grid_tiles(20,20,9,3,28,28,3,[W,"#e9f1fb"])
    floor=f'<rect x="20" y="115" width="280" height="65" fill="#dfe8f3"/>'+"".join(f'<line x1="{20+i*35}" y1="115" x2="{20+i*35}" y2="180" stroke="{GROUT}"/>' for i in range(1,8))
    drain=f'<circle cx="160" cy="150" r="10" fill="{PD}"/><circle cx="160" cy="150" r="5" fill="#9fb3c8"/>'
    arrows="".join(f'<path d="M{x} 150 L{160+(x-160)*0.45} 150" stroke="{A}" stroke-width="3" marker-end="url(#ar)"/>' for x in (60,260))
    shower=f'<path d="M250 30v30h-20" stroke="#9fb3c8" stroke-width="5" fill="none"/><rect x="214" y="58" width="32" height="8" rx="3" fill="#9fb3c8"/>'
    defs=f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8z" fill="{A}"/></marker></defs>'
    return frame(defs+clip(f'<rect x="20" y="20" width="280" height="160" fill="{GROUT}"/>'+wall+floor+drain+arrows+shower,20,20,280,160,"c4"),"تبليط حمام بميول نحو الصفاية")

def s_repair():
    t=grid_tiles(20,20,6,4,44,38,4,[W,"#eef3f9"])
    x,y=20+2*48,20+1*42
    crack=f'<rect x="{x}" y="{y}" width="44" height="38" fill="#fff4dd" stroke="{A}" stroke-width="3"/><path d="M{x+6} {y+4} l10 12 -6 6 12 10 -4 4 14 0" fill="none" stroke="{PD}" stroke-width="2"/>'
    return frame(clip(f'<rect x="20" y="20" width="280" height="160" fill="{GROUT}"/>'+t+crack,20,20,280,160,"c5"),"تغيير بلاطة مكسورة")

def s_project():
    b=f'<rect x="20" y="20" width="280" height="160" fill="#e8eef6"/>'
    for i,(x,hh) in enumerate([(50,120),(130,150),(210,100)]):
        b+=f'<rect x="{x}" y="{180-hh}" width="62" height="{hh}" fill="{[P,PD,P][i]}"/>'
        for r in range(int(hh/24)):
            for c in range(3):
                b+=f'<rect x="{x+8+c*18}" y="{180-hh+8+r*24}" width="10" height="12" fill="{[W,"#ffe7b3"][(r+c+i)%2]}"/>'
    b+=f'<rect x="20" y="176" width="280" height="4" fill="{A}"/>'
    return frame(clip(b,20,20,280,160,"c6"),"تبليط عمائر ومشاريع")

# ── أشكال التركيب 240×180 ──
def pat(body,title):
    return svg(240,180,f'<rect width="240" height="180" fill="{GROUT}"/>'+body,title)
def p_straight(): return pat(grid_tiles(0,0,6,5,38,34,3,[W,"#eef3f9"]),"تركيب مستقيم")
def p_offset(): return pat(grid_tiles(0,0,4,6,58,28,3,[W,"#eef3f9","#e3ebf5"],offset=True),"تركيب طوبي (إزاحة)")
def p_diag():
    t=grid_tiles(-120,-120,12,12,34,34,3,[W,"#eef3f9"])
    return pat(f'<g transform="rotate(45 120 90)">{t}</g>',"تركيب مائل 45 درجة")
def p_herring():
    out=[];L,S,g=60,20,3
    for r in range(-2,8):
        for c in range(-2,8):
            x=c*(L+g)-r*0+(r%2)*0; y=r*(S+g)*2
            bx=c*40+ r*0; by=r*40
            out.append(f'<rect x="{bx}" y="{by}" width="{L-g}" height="{S-g}" fill="{["#f3e6cf","#ead8b8"][(r+c)%2]}" stroke="#d1bb93"/>')
            out.append(f'<rect x="{bx+L-g-S+g}" y="{by+S}" width="{S-g}" height="{L-g}" fill="{["#ead8b8","#f3e6cf"][(r+c)%2]}" stroke="#d1bb93"/>')
    return svg(240,180,'<rect width="240" height="180" fill="#d1bb93"/><g transform="translate(-30,-60) rotate(-45 120 90)">'+"".join(out)+"</g>","تركيب هيرنج بون (بلاط خشبي)")

def write_all(outdir):
    d=os.path.join(outdir,"assets","img"); os.makedirs(d,exist_ok=True)
    files={"hero.svg":hero(),"s-ceramic.svg":s_ceramic(),"s-porcelain.svg":s_porcelain(),"s-marble.svg":s_marble(),
           "s-bath.svg":s_bath(),"s-repair.svg":s_repair(),"s-project.svg":s_project(),
           "p-straight.svg":p_straight(),"p-offset.svg":p_offset(),"p-diag.svg":p_diag(),"p-herring.svg":p_herring()}
    for n,c in files.items(): open(os.path.join(d,n),"w",encoding="utf-8").write(c)
    return list(files)
