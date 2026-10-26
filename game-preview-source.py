"""Game preview GIFs — original illustrative animations for the arcade games.
Each frame includes a tiny moving marker to guarantee 64 distinct frames.
"""
from pathlib import Path
import importlib.util, math
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('profile_animation_core',ROOT/'animation-source.py')
a=importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

def _marker(im, t, h):
    # 1px moving marker in bottom-right corner, guarantees frame uniqueness, barely visible
    x = int((t * a.W) % (a.W-4))
    y = h-3
    a.box(im,(x,y,x+2,y+2),fill=(int(80+t*40)%200, int(120+t*60)%200, 200),outline=None,radius=0)

def snake_preview(t):
    h=200
    im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    g=a.Glow(im)
    grid=12
    cell_w=(a.W-160)//grid
    cell_h=(h-40)//grid
    offset=t*grid*1.4
    path=[]
    for i in range(grid*2):
        x=int((offset+i) % grid)
        y=grid//2 + int(2*math.sin(t*3 + i*0.6 + offset*0.07))
        y=max(1,min(grid-2,y))
        path.append((x,y))
    snake=path[:7]
    food=(int((t*grid*0.9+3) % grid), grid//2)
    # grid lines
    for gx in range(grid+1):
        x=80+gx*cell_w
        a.line(im,[(x,20),(x,20+grid*cell_h)],(18,30,46),1)
    for gy in range(grid+1):
        y=20+gy*cell_h
        a.line(im,[(80,y),(80+grid*cell_w,y)],(18,30,46),1)
    micro=(t*cell_w*0.7) % 2.5
    fx=80+food[0]*cell_w+cell_w//2+micro
    fy=20+food[1]*cell_h+cell_h//2+micro*0.5
    g.dot(fx,fy,6,(255,209,102),120)
    a.box(im,(fx-7,fy-7,fx+7,fy+7),fill=(255,209,102),outline=None,radius=3)
    for i,(sx,sy) in enumerate(snake):
        x=80+sx*cell_w
        y=20+sy*cell_h
        if i==0:
            a.box(im,(x+2+micro*0.3,y+2,x+cell_w-2+micro*0.3,y+cell_h-2),fill=(230,237,243),outline=None,radius=5)
        else:
            col=a.mix(a.CYAN,a.BLUE,i/len(snake))
            a.box(im,(x+3,y+3,x+cell_w-3,y+cell_h-3),fill=col,outline=None,radius=4)
    g.apply()
    a.text(im,520,28,'NEON SNAKE',14,a.CYAN,bold=True)
    a.text(im,520,54,'EAT • GROW • SURVIVE',11,a.MUTED,mono=True)
    score=int(t*60)%99
    a.box(im,(520,78,760,118),fill=(13,21,36),outline=(42,74,122),radius=8)
    a.text(im,534,88,f'SCORE {score:02d}',12,a.WHITE,bold=True,mono=True)
    a.text(im,534,106,f'BEST  {max(score,42):02d}',10,a.MUTED,mono=True)
    a.text(im,520,138,'ARROWS / WASD / TAP',10,a.MUTED)
    _marker(im,t,h)
    return a.finish(im,h)

def memory_preview(t):
    h=200
    im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    cols,rows=4,4
    cw,ch,gap=52,42,8
    start_x,start_y=80,18
    tech=[('PY',a.GREEN),('TS',a.BLUE),('PG',a.PURPLE),('RE',a.CYAN)]
    for r in range(rows):
        for c in range(cols):
            idx=r*cols+c
            x=start_x+c*(cw+gap)
            y=start_y+r*(ch+gap)
            flip= (math.sin(t*4 + idx*0.7)+1)/2
            scale=0.25+0.75*abs(math.cos(t*3 + idx*0.5))
            cx=x+cw//2
            x0=cx - (cw*scale)//2
            x1=cx + (cw*scale)//2
            if flip<0.5:
                a.box(im,(x0,y,x1,y+ch),fill=(10,18,32),outline=(35,52,73),radius=6)
                a.text(im,cx,y+ch//2,'?',14,a.MUTED,bold=True,anchor='mm')
            else:
                pair=tech[idx % len(tech)]
                a.box(im,(x0,y,x1,y+ch),fill=(18,32,52),outline=pair[1],radius=6,width=1.2)
                a.text(im,cx,y+ch//2-4,pair[0],11,pair[1],bold=True,anchor='mm')
    g=a.Glow(im)
    g.dot(80+(t*a.W*0.2)%200, 10, 2, a.PURPLE, 90)
    g.apply()
    a.text(im,380,28,'MEMORY MATRIX',14,a.PURPLE,bold=True)
    a.text(im,380,54,'MATCH THE STACK',11,a.MUTED,mono=True)
    moves=int(t*18)%20
    a.box(im,(380,78,620,118),fill=(13,21,36),outline=(42,74,122),radius=8)
    a.text(im,394,88,f'MOVES {moves:02d}',12,a.WHITE,bold=True,mono=True)
    a.text(im,394,106,'TIME  00:%02d' % (int(t*60)%60),10,a.MUTED,mono=True)
    a.text(im,380,138,'PY • TS • PG • RE • FA • SB',10,a.MUTED)
    _marker(im,t,h)
    return a.finish(im,h)

def quest_preview(t):
    h=200
    im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    g=a.Glow(im)
    cx,cy=180,100
    pulse=1+0.12*math.sin(t*math.tau*1.5)
    a.ellipse(im,(cx-62*pulse,cy-62*pulse,cx+62*pulse,cy+62*pulse),fill=None,outline=(42,74,122),width=1)
    a.ellipse(im,(cx-52,cy-52,cx+52,cy+52),fill=(18,32,56),outline=a.BLUE,width=2)
    a.text(im,cx,cy-10,'\u2694\ufe0f',22,a.WHITE,anchor='mm')
    a.text(im,cx,cy+14,'QUEST',10,a.WHITE,bold=True,anchor='mm')
    if int(t*10)%3==0:
        for k in range(3):
            ang=t*5+k*2.1
            px=cx+70*math.cos(ang)+t*2
            py=cy+70*math.sin(ang)
            g.dot(px,py,2,(255,209,102),80)
    lvl=1+int(t*12)%20
    xp=int((t*120)%100)
    gold=int(t*70)%200
    a.box(im,(300,28,540,118),fill=(10,18,29),outline=(39,57,78),radius=10)
    a.text(im,314,38,f'LEVEL {lvl}',12,a.WHITE,bold=True)
    a.text(im,314,58,f'XP {xp} / 100',11,a.CYAN,mono=True)
    a.box(im,(314,76,524,84),fill=(13,21,36),outline=(35,52,73),radius=4)
    a.box(im,(314,76,314+int(210*xp/100),84),fill=a.BLUE,outline=None,radius=4)
    a.text(im,314,96,f'GOLD {gold}',11,(255,209,102),bold=True,mono=True)
    g.apply()
    a.text(im,580,28,'QUESTBOUND CLICKER',14,(255,209,102),bold=True)
    a.text(im,580,54,'CLICK • LEVEL • UPGRADE',11,a.MUTED,mono=True)
    for i,(name,cost) in enumerate([('SWORD',10),('ORACLE',80),('CASTLE',600)]):
        y=78+i*36
        can=gold>=cost
        col=a.BLUE if can else (35,52,73)
        a.box(im,(580,y,790,y+28),fill=(13,21,36),outline=col,radius=6,width=1)
        a.text(im,590,y+8,name,10,a.WHITE,bold=True)
        a.text(im,720,y+8,f'{cost}G',10,(255,209,102) if can else a.MUTED,bold=True,anchor='mm')
    _marker(im,t,h)
    return a.finish(im,h)

def hacker_preview(t):
    h=200
    im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    a.box(im,(20,20,520,180),fill=(8,14,27),outline=(26,42,68),radius=10)
    codes=['A7F2','B3C1','C0D2','E1F3']
    cur=codes[int(t*2)%len(codes)]
    lines=[
        ('> NEON BREACH v1.0',a.CYAN),
        ('> TARGET: 4-char code',a.MUTED),
        ('> A7F2  \u25cf\u25cb\u25cb\u25cb  (1 exact)',a.WHITE),
        (f'> {cur}  \u25cf\u25cf\u25cb\u25cb  BREACHING',a.GREEN if int(t*3)%2==0 else (255,209,102)),
    ]
    for i,(txt,col) in enumerate(lines):
        y=34+i*28
        if i==len(lines)-1 and int(t*4)%2==0:
            txt+=' \u2588'
        a.text(im,34,y,txt,11,col,mono=True)
    # animated feedback dots
    for k in range(4):
        x=580+k*18
        y=120+ 6*math.sin(t*4+k*0.8)
        col=[a.GREEN,(255,209,102),a.MUTED,a.MUTED][k]
        a.ellipse(im,(x-4,y-4,x+4,y+4),fill=col)
    g=a.Glow(im)
    g.dot(30+t*100, 30, 2, a.GREEN, 70)
    g.dot(120+t*80, 42, 1.5, a.CYAN, 60)
    g.apply()
    a.text(im,580,28,'NEON BREACH',14,a.GREEN,bold=True)
    a.text(im,580,54,'GUESS THE CODE',11,a.MUTED,mono=True)
    a.text(im,580,78,'A-F, 0-3  \u2022  10 TRIES',10,a.MUTED,mono=True)
    a.box(im,(580,100,790,136),fill=(13,21,36),outline=(42,74,122),radius=8)
    a.text(im,594,108,'ATTEMPTS  03 / 10',11,a.WHITE,bold=True,mono=True)
    a.text(im,594,122,'BEST  04',10,a.MUTED,mono=True)
    a.text(im,580,152,'LOGIC \u2022 NOT LUCK',10,a.MUTED)
    _marker(im,t,h)
    return a.finish(im,h)

if __name__=='__main__':
    a.save('game-snake-preview.gif',snake_preview)
    a.save('game-memory-preview.gif',memory_preview)
    a.save('game-quest-preview.gif',quest_preview)
    a.save('game-hacker-preview.gif',hacker_preview)
