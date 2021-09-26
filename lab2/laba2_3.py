
import numpy as np
import matplotlib.pyplot as plt
import turtle as tr
import random as rn


tr.shape('circle')
tr.speed(0)
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







#tr.hideturtle()