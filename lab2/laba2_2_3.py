import numpy as np
import matplotlib.pyplot as plt
import turtle as tr
import random as rn

def resettr():
    tr.clear()
    tr.up()
    tr.goto(-325,0)
    tr.seth(0)
    return

def numberX(A, a):
    tr.seth(-180)
    for i, j, k in zip(A, (90, 135, 225, 270, 90, 135, 225, 270, 180), (1, 1, np.sqrt(2), 1, 1, 1, np.sqrt(2), 1, 1)):
        if int(i):
            tr.down()
        tr.forward(a*k)
        tr.up()
        tr.left(j)
    tr.seth(0)
    tr.forward(2.5*a)
    tr.left(90)
    tr.forward(2*a)
    return

inp_shrift = open('/../lab2/input_laba2_2_3.txt', 'r')
a=50
y = input()
tr.shape('arrow')
tr.speed(0)
tr.hideturtle()
resettr()

x=inp_shrift.readlines()
for j in y:
    numberX(x[int(j)].rstrip() , a)
inp_shrift.close()
tr.exitonclick()
