import numpy as np
import matplotlib.pyplot as plt
import turtle as tr
import random as rn


d=[]
d.append({
    'x': -300,
    'y': -200,
    'vx': 20,
    'vy': 70,
    'r': 2,
    'it': 0
})

g=9.81
dt=0.1
R=0.95
k=0.01
d[0]['it']=tr.Turtle(shape='circle', visible=0)
d[0]['it'].shapesize(d[0]['r'])
d[0]['it'].up()
d[0]['it'].goto(-300, -200)
d[-1]['it'].showturtle()
d[0]['it'].speed(0)
for i in range(10000):
    for j in range(len(d)):
        d[j]['x']+=d[j]['vx']*dt
        d[j]['y']+=d[j]['vy']*dt
        d[j]['vx']-=k*d[j]['vx']*dt
        d[j]['vy']-=k*d[j]['vy']*dt+g*dt
        d[j]['it'].goto( d[j]['x'], d[j]['y'])
        if d[j]['y']<-200:
            d[j]['vy']=-R*d[j]['vy']
            d[j]['y']=-200
            st=0.2+0.6*rn.random()
            d.append({})
            d[-1]=d[j].copy()
            print(d[-1] is d[j])

            d[-1]['r']*=(1-st)
            d[j]['r']*=st

            d[-1]['it']=tr.Turtle(shape='circle', visible = 0)
            d[-1]['it'].shapesize(d[-1]['r'])
            d[j]['it'].shapesize(d[j]['r'])
            d[-1]['vx']*=-(1-st)
            d[j]['vx']*=st
            d[j]['vy']*=(2-st)
            d[-1]['it'].up()

            d[-1]['it'].goto( d[-1]['x'], d[-1]['y'])
            d[-1]['it'].showturtle()
        
tr.exitonclick()   




"""

x=-300
y=0
k=0.05
tr.goto(300,-1)
tr.width(2)
tr.down()
tr.goto(x,-1)
tr.width(1)
eta=0.9
g=9.81
dt=0.1
vx=30
vy=70
for i in range(2000):

    x+=vx*dt
    y+=vy*dt
    if y<0:
        vy=-eta*vy+2*g*dt
    else:
        vy-=g*dt+k*vy*dt
    vx-=k*vx*dt
    tr.goto(x,y)
"""