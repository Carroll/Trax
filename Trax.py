#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=6 expandtab shiftwidth=3 softtabstop=3
from __future__ import print_function
import sys
import time
try:
   import Tkinter as tk
except:
   import tkinter as tk

if len(sys.argv) > 1:
   gamestring = sys.argv[1]
else:
   gamestring="@0/ B1+ C1/ B0/ B3\ @3\ E2/ E1/ E4\ F2+ E0/ G1\ F0+ C6+ G4\ G0+ H1+ G0\ I3\ J3\ H7\ H8\ D9+ C10\ F9\ F10\ F11\ E12+ C11+ H10+ G12+ H5+ I6+ I9+ J6/ K8/ A9/ @8\ E13\ C10+ E14+ E15\ E16\ C14\ C12+ B11+ C15+ B14/ A14+ @14\ B15\ J13+ K10\ J14/ I14\ G14+ M6/ K5+ L10+ N5+ O4\ N3+ M2+ P3/ N2/ N8\ O9/ I0/ J1/ N2/ I0\ H1\ Q5+ M2/ E5\ D5\ N12\ P12+ Q11+ R10+ P13\ Q13\ K1/ I0+ H0/ H0/ H0/ G1/ H0+ G0+ F1+ G0/ E3/ D3/ F5/ E4+ H10+ G8+ E8+ G11+ C3/"

c=gamestring.replace(' ','')
game=list(c)


Label = []
Moves = []

T=[[('',True),('',True),('',True),('',True)],
   [('',True),('',True),('',True),('',True)],
   [('',True),('',True),('',True),('',True)],
   [('',True),('',True),('',True),('',True)]
   ]

colors = ["White", "Black"]

def coord(x,y,string):
    label = tk.Label(canvas, text=string, bg="light green")
    label.place(x=size/2-5+x*size,y=size/2-5+y*size)
    Label.append(label)

def slashg(x,y,sens,color):
    canvas.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size,fill="red",outline="grey",width=2)
    if not sens:
       if color==0:
          canvas.create_circle_arc(x*size, y*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=270, end=360)
          canvas.create_circle_arc((x+1)*size, (y+1)*size, size/2, fill="red", outline="light green", style=tk.ARC, width=wb, start=90, end=180)
       else:
          canvas.create_circle_arc(x*size, y*size, size/2, fill="red", outline="green", style=tk.ARC, width=bb, start=270, end=360)
          canvas.create_circle_arc((x+1)*size, (y+1)*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=90, end=180)
    else:
       if color==0:
          canvas.create_circle_arc(x*size, y*size, size/2, fill="red", outline="light green", style=tk.ARC, width=wb, start=270, end=360)
          canvas.create_circle_arc((x+1)*size, (y+1)*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=90, end=180)
       else:
          canvas.create_circle_arc(x*size, y*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=270, end=360)
          canvas.create_circle_arc((x+1)*size, (y+1)*size, size/2, fill="red", outline="green", style=tk.ARC, width=bb, start=90, end=180)

def backslashg(x,y,sens,color):
    canvas.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size,fill="red",outline="grey",width=2)
    if not sens:
       if color==0:
          canvas.create_circle_arc((x+1)*size, y*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=180, end=270)
          canvas.create_circle_arc(x*size, (y+1)*size, size/2, fill="red", outline="light green", style=tk.ARC, width=wb, start=0, end=90)
       else:
          canvas.create_circle_arc((x+1)*size, y*size, size/2, fill="red", outline="green", style=tk.ARC, width=bb, start=180, end=270)
          canvas.create_circle_arc(x*size, (y+1)*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=0, end=90)
    else:
       if color==0:
          canvas.create_circle_arc((x+1)*size, y*size, size/2, fill="red", outline="light green", style=tk.ARC, width=wb, start=180, end=270)
          canvas.create_circle_arc(x*size, (y+1)*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=0, end=90)
       else:
          canvas.create_circle_arc((x+1)*size, y*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=180, end=270)
          canvas.create_circle_arc(x*size, (y+1)*size, size/2, fill="red", outline="green", style=tk.ARC, width=bb, start=0, end=90)
  
def plusg(x,y,sens,color):
    canvas.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size,fill="red",outline="grey",width=2)
    if sens:
        if color==0:
           canvas.create_line(x*size+size/2,y*size,x*size+size/2,(y+1)*size,fill="light green", width=wb)
           canvas.create_line(x*size,y*size+size/2,(x+1)*size,y*size+size/2,fill="black", width=bb)
        else:
           canvas.create_line(x*size+size/2,y*size,x*size+size/2,(y+1)*size,fill="white", width=wb)
           canvas.create_line(x*size,y*size+size/2,(x+1)*size,y*size+size/2,fill="green", width=bb)
    else:
        if color==0:
           canvas.create_line(x*size,y*size+size/2,(x+1)*size,y*size+size/2,fill="light green", width=wb)
           canvas.create_line(x*size+size/2,y*size,x*size+size/2,(y+1)*size,fill="black", width=bb)
        else:
           canvas.create_line(x*size,y*size+size/2,(x+1)*size,y*size+size/2,fill="white", width=wb)
           canvas.create_line(x*size+size/2,y*size,x*size+size/2,(y+1)*size,fill="green", width=bb)
       

def slash(x,y,sens):
    canvas.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size,fill="red",outline="grey",width=2)
    if not sens:
        canvas.create_circle_arc(x*size, y*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=270, end=360)
        canvas.create_circle_arc((x+1)*size, (y+1)*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=90, end=180)
    else:
        canvas.create_circle_arc(x*size, y*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=270, end=360)
        canvas.create_circle_arc((x+1)*size, (y+1)*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=90, end=180)

def backslash(x,y,sens):
    canvas.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size,fill="red",outline="grey",width=2)
    if not sens:
        canvas.create_circle_arc((x+1)*size, y*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=180, end=270)
        canvas.create_circle_arc(x*size, (y+1)*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=0, end=90)
    else:
        canvas.create_circle_arc((x+1)*size, y*size, size/2, fill="red", outline="white", style=tk.ARC, width=wb, start=180, end=270)
        canvas.create_circle_arc(x*size, (y+1)*size, size/2, fill="red", outline="black", style=tk.ARC, width=bb, start=0, end=90)
  
def plus(x,y,sens):
    canvas.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size,fill="red",outline="grey",width=2)
    if sens:
        canvas.create_line(x*size+size/2,y*size,x*size+size/2,(y+1)*size,fill="white", width=wb)
        canvas.create_line(x*size,y*size+size/2,(x+1)*size,y*size+size/2,fill="black", width=bb)
    else:
        canvas.create_line(x*size,y*size+size/2,(x+1)*size,y*size+size/2,fill="white", width=wb)
        canvas.create_line(x*size+size/2,y*size,x*size+size/2,(y+1)*size,fill="black", width=bb)
       
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)

def affich():
    global size,wb,bb
    canvas.config(width=size*(len(TT[0])+.5),height=size*(len(TT)))
    size=min(60,height/(len(TT)+correct))
    wb=size/8
    bb=size/8+1
    row = '0/'
    r0=ord(row[0])-48
    r1=ord(row[1])-48
    for j in range(0,len(TT)-1):
        if r0==0: row = ' '+chr(r1+48)
        else: row = chr(r0+48)+chr(r1+48)
        if j>0:
            coord(0,j,row)
            coord(len(TT[0])-1,j,row)
        r1+=1
        if r1>9:
            r1-=10
            r0+=1
            row = chr(r0+48)+chr(r1+48)
    col='?'
    for i in range(0,len(TT[0])-1):
        if i>0:
            coord(i,0,col)
            coord(i,len(TT)-1,col)
        col=chr(ord(col)+1)
    for j in range(len(TT)):
        for i in range(len(TT[j])):
            t = invConc[invTupDic[TT[j][i]]]
            if t[0]=='/':
                slash(i,j,t[1])
            elif t[0]=='\\':
                backslash(i,j,t[1])
            elif t[0]=='+':
                plus(i,j,t[1])
                
def checkWin(x,y):
    # check white path (0) and then black (1)
    win = False
    colorWin = 2
    for color in range(2):
       xp,yp=x,y
       loop = True
       colorGreen = False
       edge=0
       while loop:
          try:
             if abs(edge-TT[yp][xp].index(color))==2:
                edge = 3-TT[yp][xp][::-1].index(color)
             else:
                edge = TT[yp][xp].index(color)
          except:
             loop = False
             break
          if edge==0: yp-=1
          elif edge==1: xp+=1
          elif edge==2: yp+=1
          elif edge==3: xp-=1
          if xp==x and yp==y:
             if colorGreen:
                loop = False
             else:
                colorGreen = True          
                win = True
                colorWin = color
                print ("Loop for color",colors[colorWin])
          if colorGreen:
             t = invConc[invTupDic[TT[yp][xp]]]
             if t[0]=='/':
                slashg(xp,yp,t[1],color)
             elif t[0]=='\\':
                backslashg(xp,yp,t[1],color)
             elif t[0]=='+':
                plusg(xp,yp,t[1],color)
             canvas.update_idletasks()
             #import pdb; pdb.set_trace()
    if win: 
        time.sleep(3)
    return win,colorWin

def restoreTT():
    TT=[] #save
    for j in range(len(TS)):
        TT.append([])
        TT[j][:] = TS[j][:]

def coupForceN(x,y): # after playing at x,y we look in the 4 directions, north east south west
    valid = True
    put = False
    a,b = x,y # pour decalage
    global TT,TS
    TS=[] #save
    for j in range(len(TT)):
        TS.append([])
        TS[j][:] = TT[j][:]
    t=TT[y][x]
    c = t[0] # couleur à matcher vers Nord
    if TT[y-1][x] == (2,2,2,2): # verif de case vide sinon pas possible
        t2n = TT[y-2][x] # deux au nord
        if t2n[2]==c: # face sud 2 plus loin bonne couleur
            plus = (c,1-c,c,1-c)
            #verif valid ouest et est
            if TT[y-1][x-1][1] != 2 and TT[y-1][x-1][1] != 1-c or TT[y-1][x+1][3] != 2 and TT[y-1][x+1][3] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y-1][x] = plus
            put = True
            #if y-1==1:
            #    TT.insert(0,len(T[0])*[(2,2,2,2)])
            #    b+=1
            valid = coupForce(a,b-1)
        tno = TT[y-1][x-1] # case NO
        if tno[1]==c: # face est de case NO
            back = (1-c,1-c,c,c)
            #verif valid nord et est
            if TT[y-2][x][2] != 2 and TT[y-2][x][2] != 1-c or TT[y-1][x+1][3] != 2 and TT[y-1][x+1][3] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y-1][x] = back
            put = True
            valid = coupForce(a,b-1)
        tne = TT[y-1][x+1] # case NE
        if tne[3]==c: # face ouest de case NE
            slash = (1-c,c,c,1-c)
            #verif valid nord et ouest
            if TT[y-2][x][2] != 2 and TT[y-2][x][2] != 1-c or TT[y-1][x-1][1] != 2 and TT[y-1][x-1][1] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y-1][x] = slash
            put = True
            valid = coupForce(a,b-1)

    c = t[1] # couleur à matcher vers l'est
    if TT[y][x+1] == (2,2,2,2): # verif de case vide sinon pas possible
        if x+2<len(TT[0]):
            t2e = TT[y][(x+2)%len(TT[0])] # deux a l'est
            if t2e[3]==c: # face ouest 2 plus loin bonne couleur
                plus = (1-c,c,1-c,c)
                #verif valid sud et nord
                if TT[y-1][x+1][2] != 2 and TT[y-1][x+1][2] != 1-c or TT[y+1][x+1][0] != 2 and TT[y+1][x+1][0] != 1-c:
                    #remettre TS
                    restoreTT()
                    return False,False
                TT[y][x+1] = plus
                put = True
                #if x>=len(TT[0])-2:
                #    for i in TT:
                #        i.append((2,2,2,2))
                
                valid = coupForce(a+1,b)
        tne = TT[y-1][x+1] # case NE
        if tne[2]==c: # face sud de case NE
            slash = (c,1-c,1-c,c)
            #verif valid sud et est
            if TT[y][x+2][3] != 2 and TT[y][x+2][3] != 1-c or TT[y+1][x+1][0] != 2 and TT[y+1][x+1][0] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y][x+1] = slash
            put = True
            valid = coupForce(a+1,b)
        tse = TT[y+1][x+1] # case SE
        if tse[0]==c: # face nord de case SE
            back = (1-c,1-c,c,c)
            #verif valid nord et est
            if TT[y][x+2][3] != 2 and TT[y][x+2][3] != 1-c or TT[y-1][x+1][2] != 2 and TT[y-1][x+1][2] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y][x+1] = back
            put = True
            valid = coupForce(a+1,b)

    c = t[2] # couleur à matcher vers Sud
    if TT[y+1][x] == (2,2,2,2): # verif de case vide sinon pas possible
        t2s = TT[(y+2)%len(TT)][x] # deux au sud
        if t2s[0]==c: # face nord 2 plus loin bonne couleur
            plus = (c,1-c,c,1-c)
            #verif valid ouest et est
            if TT[y+1][x+1][3] != 2 and TT[y+1][x+1][3] != 1-c or TT[y+1][x-1][1] != 2 and TT[y+1][x-1][1] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y+1][x] = plus
            put = True
            # if y+1==len(TT)-1:
            #    TT.append(len(T[0])*[(2,2,2,2)])
            valid = coupForce(a,b+1)
        tse = TT[y+1][x+1] # case SE
        if tse[3]==c: # face ouest de case SE
            back = (c,c,1-c,1-c)
            #verif valid sud et ouest
            if TT[y+2][x][0] != 2 and TT[y+2][x][0] != 1-c or TT[y+1][x-1][1] != 2 and TT[y+1][x-1][1] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y+1][x] = back
            put = True
            valid = coupForce(a,b+1)
        tso = TT[y+1][x-1] # case SO
        if tso[1]==c: # face est de case SO
            slash = (c,1-c,1-c,c)
            #verif valid sud et est
            if TT[y+2][x][0] != 2 and TT[y+2][x][0] != 1-c or TT[y+1][x+1][3] != 2 and TT[y+1][x+1][3] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y+1][x] = slash
            put = True
            valid = coupForce(a,b+1)

    c = t[3] # couleur à matcher vers ouest
    if TT[y][x-1] == (2,2,2,2): # verif de case vide sinon pas possible
        t2o= TT[y][x-2] # deux a l'ouest
        if t2o[1]==c: # face est 2 plus loin bonne couleur
            plus = (1-c,c,1-c,c)
            #verif valid sud et nord
            if TT[y+1][x-1][0] != 2 and TT[y+1][x-1][0] != 1-c or TT[y-1][x-1][2] != 2 and TT[y-1][x-1][2] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y][x-1] = plus
            put = True
            #if y-1==1:
            #    TT.insert(0,len(T[0])*[(2,2,2,2)])
            #    b+=1
            valid = coupForce(a-1,b)
        tno = TT[y-1][x-1] # case NO
        if tno[2]==c: # face sud de case NO
            back = (c,c,1-c,1-c)
            #verif valid ouest et sud
            if TT[y][x-2][1] != 2 and TT[y][x-2][1] != 1-c or TT[y+1][x-1][0] != 2 and TT[y+1][x-1][0] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y][x-1] = back
            put = True
            valid = coupForce(a-1,b)
        tso = TT[y+1][x-1] # case SO
        if tso[0]==c: # face nord de case SO
            slash = (1-c,c,c,1-c)
            #verif valid nord et ouest
            if TT[y][x-2][1] != 2 and TT[y][x-2][1] != 1-c or TT[y-1][x-1][2] != 2 and TT[y-1][x-1][2] != 1-c:
                #remettre TS
                restoreTT()
                return False,False
            TT[y][x-1] = slash
            put = True
            valid = coupForce(a-1,b)

    return valid,put

def coupForce(x,y):
    """ Checks for forced moves and then win completion, returns True if the forced move was valid """
    global TT,TS
    a,b = x,y
    valid = True
    TS=[] #save
    for j in range(len(TT)):
        TS.append([])
        TS[j][:] = TT[j][:]
    valid,put = coupForceN(a,b)
    if not valid:
        restoreTT()
        return False
    if put:
         win,colorWin=checkWin(x,y);
    return valid

def mettreT(x,y,t):
    global TT
    valid = True
    TS=[] #save
    for j in range(len(TT)):
        TS.append([])
        TS[j][:] = TT[j][:]
    f=t[0]
    #print (t,Conc[t])
    tup = TupDic[Conc[t]]
    if TT[y-1][x][2] !=2 and TT[y-1][x][2] != tup[0] or TT[y+1][x][0] !=2 and TT[y+1][x][0] != tup[2] or\
       TT[y][x-1][1] !=2 and TT[y][x-1][1] != tup[3] or TT[y][x+1][3] !=2 and TT[y][x+1][3] != tup[1]:
            valid = False
            tup = TupDic[Conc[(f,False)]]
            if TT[y-1][x][2] !=2 and TT[y-1][x][2] != tup[0] or TT[y+1][x][0] !=2 and TT[y+1][x][0] != tup[2] or\
               TT[y][x-1][1] !=2 and TT[y][x-1][1] != tup[3] or TT[y][x+1][3] !=2 and TT[y][x+1][3] != tup[1]:
                valid = False
            else:
                TT[y][x] = tup
                win,colorWin=checkWin(x,y);
                valid = coupForce(x,y)
    else:
        TT[y][x] = tup
        win,colorWin=checkWin(x,y);
        valid = coupForce(x,y)
    if valid:
        if x==1:
            for i in TT:
                i.insert(0,(2,2,2,2))
        if x>=len(TT[0])-2:
            for i in TT:
                i.append((2,2,2,2))
        if y==1:
            TT.insert(0,len(TT[0])*[(2,2,2,2)])
        if y>=len(TT)-2:
            TT.append(len(TT[0])*[(2,2,2,2)])
    else: 
        TT=TS
        print("Non valid move",x,y,t)
    return valid


root = tk.Tk()
canvas = tk.Canvas(root, width=100, height=100, borderwidth=0, highlightthickness=0, bg="light green")
canvas.grid()

tk.Canvas.create_circle_arc = _create_circle_arc

TupDic = {0:(0,1,1,0),1:(1,0,0,1),2:(0,0,1,1),3:(1,1,0,0),4:(0,1,0,1),5:(1,0,1,0),6:(2,2,2,2)}
invTupDic = {v:k for k,v in TupDic.items()}
Conc = {('/',True):0,('/',False):1,('\\',True):2,('\\',False):3,('+',True):4,('+',False):5,('',True):6}
invConc = {v:k for k,v in Conc.items()}

height = root.winfo_screenheight()-20 # window bar thickness
correct=0.4
TT=[]
TS=[]
for j in range(len(T)):
    L=[]
    for i in range(len(T[j])):
        L.append(TupDic[Conc[T[j][i]]])
    TT.append(L)
size=min(60,height/(len(TT)+correct))
wb=size/8
bb=size/8+1
valid = True
# game is a string of triplets XYT with Type \\ instead of \ 
while len(game)>0:
    x=ord(game.pop(0))-63
    y=ord(game.pop(0))-ord('0')
    t=game.pop(0)
    if t=='/' or t=='\\' or t=='+':
        y+=1
    else:
        y=1+10*y+ord(t)-ord('0')
        t=game.pop(0)
    valid = mettreT(x,y,(t,True))
    if valid:
        Moves.append((x,y,(t,True)))
    else:
        valid = mettreT(x,y,(t,False))
        if valid:
            Moves.append((x,y,(t,False)))

size=min(60,height/(len(TT)+correct))
affich()    

move = ''
while move != 'q':
    if sys.version[0]=='2': move = raw_input("move? ")
    else: move = input("move? ")
    if move=="" or move=="@@":
       print("undoing...")
       if Moves != []:
           Moves.pop(-1)
       TT=[]
       for j in range(len(T)):
           L=[]
           for i in range(len(T[j])):
               L.append(TupDic[Conc[T[j][i]]])
           TT.append(L)
       for move in Moves:
           mettreT(*(move))
    else:
        cx = move[0].upper()
        cy = move[1].upper()
        t = move[2]
        x = ord(cx)-63
        y = ord(cy)-ord('0')
        if t=='/' or t=='\\' or t=='+':
            y+=1
        else:
            y=1+10*y+ord(t)-ord('0')
            t=move[3]
        valid = mettreT(x,y,(t,True))
        if valid:
             Moves.append((x,y,(t,True)))
        else:
            valid = mettreT(x,y,(t,False))
            if valid:
                Moves.append((x,y,(t,False)))
    canvas.delete("all")
    # todo : replace by other method as label.destroy takes too much time
    for label in Label:
        label.destroy()
    Label = []
    size=min(60,height/(len(TT)+correct))
    affich()    


root.wm_title("Trax Game")
root.mainloop()

