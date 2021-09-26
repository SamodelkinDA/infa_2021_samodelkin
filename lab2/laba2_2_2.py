import numpy as np
import matplotlib.pyplot as plt
import turtle as tr
import random as rn
import pathlib

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


inp = open(pathlib.Path("infa_2021_samodelkin", "lab2", "input_laba2_2_2.txt"), 'r')
a=50
x = inp.readlines()
inp.close()
tr.shape('arrow')
tr.speed(0)
tr.hideturtle()
resettr()
for i in x:
    numberX(i.rstrip() , a)
tr.exitonclick()


