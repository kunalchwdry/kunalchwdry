"""Preview GIFs for 8 new games — original illustrative animations."""
from pathlib import Path
import importlib.util, math
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('profile_animation_core',ROOT/'animation-source.py')
a=importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

def _marker(im,t,h):
    x=int((t*a.W)%(a.W-4)); y=h-3
    a.box(im,(x,y,x+2,y+2),fill=(int(80+t*40)%200,int(120+t*60)%200,200),outline=None,radius=0)

def preview_2048(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    # 4x4 grid merging
    for r in range(4):
        for c in range(4):
            x=60+c*58; y=20+r*44
            val=[0,2,4,8,16,32,64,128,256,512,1024,2048][int((t*6 + r*2 + c)%12)]
            col=[(13,21,36),(26,42,68),(42,74,122),(57,166,255),(163,113,247),(255,209,102)][int(val).bit_length()%6] if val!=0 else (13,21,36)
            a.box(im,(x,y,x+48,y+36),fill=col if val!=0 else (13,21,36),outline=(35,52,73),radius=6)
            if val!=0:
                a.text(im,x+24,y+18,str(val),10,a.WHITE,bold=True,anchor='mm')
    g=a.Glow(im); g.dot(80+t*30,30,2,a.BLUE,80); g.apply()
    a.text(im,360,28,'TECH 2048',14,(255,209,102),bold=True)
    a.text(im,360,54,'MERGE THE STACK',11,a.MUTED,mono=True)
    a.text(im,360,78,'PY • TS • PG • RE → 2048',10,a.MUTED)
    _marker(im,t,h); return a.finish(im,h)

def preview_tetris(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    # falling tetromino
    cols=10; cell=12
    for r in range(12):
        for c in range(cols):
            x=60+c*cell; y=20+r*cell
            filled=(r>8 or (int(t*4)%2==0 and r==8 and c in [4,5])) or (r==int(t*12)%12 and c==5)
            if filled:
                col=[a.CYAN,a.BLUE,a.PURPLE,a.GREEN][(r+c)%4]
                a.box(im,(x,y,x+cell-1,y+cell-1),fill=col,outline=None,radius=2)
    # current piece
    px=60+4*cell; py=20+int((t*8)%8)*cell
    for dx,dy in [(0,0),(1,0),(0,1),(1,1)]:
        a.box(im,(px+dx*cell,py+dy*cell,px+dx*cell+cell-1,py+dy*cell+cell-1),fill=(255,209,102),outline=None,radius=2)
    a.text(im,260,28,'STACK BUILDER',14,a.PURPLE,bold=True)
    a.text(im,260,54,'TETRIS • CLEAN STACKS',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

def preview_mines(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    for r in range(6):
        for c in range(8):
            x=60+c*28; y=20+r*28
            revealed=(r+c+int(t*3))%5==0
            if revealed:
                a.box(im,(x,y,x+24,y+24),fill=(13,21,36),outline=(35,52,73),radius=4)
                if (r*c)%7==0:
                    a.text(im,x+12,y+12,'💣',10,a.WHITE,anchor='mm')
                else:
                    a.text(im,x+12,y+12,str((r+c)%4+1),10,a.BLUE,bold=True,anchor='mm')
            else:
                a.box(im,(x,y,x+24,y+24),fill=(18,26,40),outline=(35,52,73),radius=4)
    a.text(im,360,28,'CODE MINES',14,(248,81,73),bold=True)
    a.text(im,360,54,'FIND BUGS • FLAG THEM',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

def preview_flappy(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    bird_y=80+30*math.sin(t*4)
    a.ellipse(im,(120-10,bird_y-10,120+10,bird_y+10),fill=(230,237,243))
    # pipes
    for k in range(3):
        x=200+k*180 - int(t*80)%180
        gap_top=30+int((t*3+k*1.3)%3*18)
        gap=70
        top_h=gap_top
        bot_y=20+gap_top+gap
        if bot_y>175: bot_y=175
        if top_h<10: top_h=10
        a.box(im,(x,20,x+40,20+top_h),fill=(26,42,68),outline=None,radius=4)
        a.box(im,(x,bot_y,x+40,180),fill=(26,42,68),outline=None,radius=4)
    g=a.Glow(im); g.apply()
    a.text(im,360,28,'FLAPPY CODE',14,a.CYAN,bold=True)
    a.text(im,360,54,'FLAP THROUGH { } [ ]',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

def preview_bug(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    for i in range(6):
        x=60+ (i*110 + int(t*100))%500
        y=40+ int(50*math.sin(t*3+i))
        is_bad=i%3==0
        col=(248,81,73) if is_bad else (63,185,80)
        a.ellipse(im,(x-16,y-16,x+16,y+16),fill=(26,42,40) if not is_bad else (42,26,26),outline=col,width=1.5)
        a.text(im,x,y,'✨' if is_bad else '🐛',12,col,anchor='mm')
    a.text(im,360,28,'BUG SQUASHER',14,a.GREEN,bold=True)
    a.text(im,360,54,'SQUASH BUGS • AVOID FEATURES',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

def preview_typing(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    code="const quest = await db.select().from(quests);"
    for i,ch in enumerate(code[:30]):
        x=60+i*9; y=60
        done=i<int(t*20)%30
        col=a.GREEN if done else a.MUTED
        a.text(im,x,y,ch,11,col,mono=True)
    # cursor
    cur=int(t*20)%30
    a.box(im,(60+cur*9,76,60+cur*9+8,78),fill=a.BLUE,outline=None,radius=1)
    a.text(im,360,28,'TYPING BLITZ',14,a.CYAN,bold=True)
    a.text(im,360,54,'TYPE CODE • WPM • ACCURACY',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

def preview_dungeon(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    for r in range(7):
        for c in range(7):
            x=60+c*22; y=20+r*22
            wall=(r==0 or c==0 or r==6 or c==6 or (r==3 and c in [2,4]))
            if wall:
                a.box(im,(x,y,x+18,y+18),fill=(18,26,40),outline=(35,52,73),radius=3)
            else:
                a.box(im,(x,y,x+18,y+18),fill=(13,21,36),outline=(26,42,68),radius=3)
    # player moving
    px=60+int((t*3)%5)*22; py=20+int((t*2)%5)*22
    a.box(im,(px,py,px+18,py+18),fill=(18,32,56),outline=a.CYAN,radius=4,width=1.5)
    a.text(im,px+9,py+9,'⚔️',10,a.CYAN,anchor='mm')
    a.text(im,260,28,'DUNGEON CRAWLER',14,(255,209,102),bold=True)
    a.text(im,260,54,'QUESTBOUND • FLOORS • GOLD',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

def preview_runner(t):
    h=200; im=a.base(h)
    a.box(im,(1,1,a.W-1,h-1),fill=None,outline=(35,52,73),radius=12)
    # ground
    a.line(im,[(60,150),(300,150)],(35,52,73),2)
    # player jumping
    py=130+ int(20*abs(math.sin(t*4)) ) if int(t*2)%3!=0 else 110
    a.box(im,(80,py,100,py+20),fill=(230,237,243),outline=None,radius=3)
    # obstacles
    for k in range(3):
        x=160+k*80 - int(t*60)%80
        a.box(im,(x,130,x+14,150),fill=(248,81,73),outline=None,radius=2)
    # xp orbs
    for k in range(2):
        x=200+k*120 - int(t*60)%120
        y=100+ int(10*math.sin(t*3+k))
        a.ellipse(im,(x-6,y-6,x+6,y+6),fill=(255,209,102))
    a.text(im,360,28,'XP RUNNER',14,(255,209,102),bold=True)
    a.text(im,360,54,'RUN • JUMP • COLLECT XP',11,a.MUTED,mono=True)
    _marker(im,t,h); return a.finish(im,h)

if __name__=='__main__':
    a.save('game-2048-preview.gif',preview_2048)
    a.save('game-tetris-preview.gif',preview_tetris)
    a.save('game-mines-preview.gif',preview_mines)
    a.save('game-flappy-preview.gif',preview_flappy)
    a.save('game-bug-preview.gif',preview_bug)
    a.save('game-typing-preview.gif',preview_typing)
    a.save('game-dungeon-preview.gif',preview_dungeon)
    a.save('game-runner-preview.gif',preview_runner)
