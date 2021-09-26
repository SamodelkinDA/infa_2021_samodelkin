
import numpy as np
import matplotlib.pyplot as plt
import turtle as tr
import random as rn

def figtr(n, a): 
    tr.up()
    tr.goto(a, 0)
    tr.down()
    for i in range(1,n+1):
        tr.goto(a*np.cos(i*2*np.pi/n),a*np.sin(i*2*np.pi/n))



def resettr():
    tr.clear()
    tr.up()
    tr.goto(0,0)
    tr.down()
    tr.seth(0)
    return


tr.shape('arrow')
tr.speed(0)

tr.pendown()
tr.color("blue")
for i in range(72):
    tr.forward(5)
    tr.right(5) 
    
resettr()

for i in range(1000):
    tr.right(rn.random()*360)
    tr.forward(rn.random()*10)



resettr()

tr.begin_fill()
tr.color("yellow")
tr.circle(-100)
tr.end_fill()
tr.up()
tr.goto(-40, -50)
tr.down()
tr.begin_fill()
tr.color("blue")
tr.circle(-13)
tr.end_fill()
tr.up()
tr.goto(40, -50)
tr.down()
tr.begin_fill()
tr.color("blue")
tr.circle(-13)
tr.end_fill()
tr.up()
tr.goto(0, -60)
tr.down()
tr.width(8)
tr.color("black")
tr.goto(0, -120)
tr.up()
tr.goto(50, -150)
tr.down()
tr.color("red")
tr.right(40)
tr.stamp()
tr.right(180)
tr.circle(80, 80)

tr.width(1)
tr.color("blue")
tr.seth(0)

resettr()

for i in range(3,12):
    figtr(i, (i-2)*10)

resettr()

for i in range(6):
    tr.circle(50)
    tr.left(60)


resettr()

tr.left(90) 
for i in range(20,121,10):
    tr.circle(i)
    tr.circle(-i)

resettr()

tr.left(90) 
for i in range(360):
    tr.goto(25*np.sin(i*2*np.pi/60)+0.5*i,25*(1-np.cos(i*2*np.pi/60)))

resettr()

n_ex13 = 11
tr.up()
tr.goto(50,0)
tr.down()
for i in range(1,n_ex13+1):
    tr.goto(50*np.cos(i*np.pi*(1-1/n_ex13)),50*np.sin(i*np.pi*(1-1/n_ex13)))

resettr()

tr.speed(0)

tr.pendown()
tr.color("blue")
tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)
tr.right(90)
tr.forward(50)
tr.right(90)
tr.forward(50)

resettr()

tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)
tr.left(90)
tr.forward(50)

resettr()

tr.seth(0)
tr.speed(0)
for i in range(10):
    a=10*(i+1)
    tr.up()
    tr.goto(-a,-a)
    tr.down()
    
    tr.forward(2*a)
    tr.left(90)
    tr.forward(2*a)
    tr.left(90)
    tr.forward(2*a)
    tr.left(90)
    tr.forward(2*a)
    tr.left(90)

resettr()

tr.speed(0)
#natural = int(input())
natural = 12
for xi in range(natural):
    tr.forward(100)
    tr.stamp()
    tr.left(180)
    tr.forward(100)
    tr.left(180)
    tr.left(360/natural)

resettr()

k=0.4
for i in range(360):
    tr.goto(k*i*np.cos(i*np.pi/36),k*i*np.sin(i*np.pi/36))

resettr()

K=20
for i in range(10):
    tr.goto(K*i,K*(i+0.25))
    tr.goto(-K*(i+0.5),K*(i+0.25))
    tr.goto(-K*(i+0.5),-K*(i+0.75))
    tr.goto(K*(i+1),-K*(i+0.75))

resettr()

tr.exitonclick()



