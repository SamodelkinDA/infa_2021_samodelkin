
import numpy as np
import matplotlib.pyplot as plt
import turtle as tr
import random as rn





num_of_tr=10
d=400
time=1000
x=[0]*num_of_tr
y=[0]*num_of_tr
vx=[0]*num_of_tr
vy=[0]*num_of_tr
for i in range(num_of_tr):
    x[i]=rn.randint(-100, 100)
    y[i]=rn.randint(-100, 100)
    vx[i]=rn.randint(-5, 5)
    vy[i]=rn.randint(-5, 5)
pool = [tr.Turtle(shape='circle') for i in range(num_of_tr)]
for j in range(len(pool)):
    pool[j].penup()
    pool[j].speed(50)
    pool[j].goto(x[j], y[j])
dt=0.3
s=1
r=1
for i in range(time):
    ax=[0]*num_of_tr
    ay=[0]*num_of_tr
    for j in range(num_of_tr):
        for k in range(j+1,num_of_tr):
           if (x[j]-x[k])**2+(y[j]-y[k])**2<=d:
                ax[j]=5*(x[j]-x[k])
                ax[k]=-5*(x[j]-x[k])
                ay[j]=5*(y[j]-y[k])
                ay[k]=-5*(y[j]-y[k])
        if x[j]**2>10000:
            ax[j]-=s*x[j]+r*vx[j]
        if y[j]**2>10000:
            ay[j]-=s*y[j]+r*vy[j]
        vx[j]+=ax[j]*dt
        vy[j]+=ay[j]*dt
        x[j]+=vx[j]*dt
        y[j]+=vy[j]*dt
        pool[j].goto(x[j], y[j])


tr.exitonclick()


