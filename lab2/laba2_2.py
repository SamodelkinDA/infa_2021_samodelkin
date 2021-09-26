
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
    for i in range(len(A)):
        if A[i]:
            tr.down()
        if (i == 2 or i== 6):
            tr.forward(a*np.sqrt(2))
        else:
            tr.forward(a)
        tr.up()
        if (i==0 or i==4):
            tr.left(90)
        if (i==1 or i==5):
            tr.left(135)
        if (i==2 or i==6):
            tr.right(135)
        if (i==3 or i==7):
            tr.right(90)
    tr.seth(0)
    tr.forward(2.5*a)
    tr.left(90)
    tr.forward(2*a)
    return



# считывание из файла в заданной папке
inp = open('/../lab3/input_laba2_2.txt', 'r')
x = inp.readlines()
inp.close()

a=50
tr.shape('arrow')
tr.speed(0)
tr.hideturtle()
for j in range(len(x)):
    x[j]=x[j].rstrip()
    resettr()
    d={"1":[0, 0, 0, 1, 0, 0, 0, 1, 0],
        "2":[1, 0, 0, 1, 1, 1, 0, 0, 1], 
        "3":[1, 0, 0, 1, 1, 0, 0, 1, 1],
        "4":[0, 1, 0, 1, 1, 0, 0, 1, 0],
        "5":[1, 1, 0, 0, 1, 0, 0, 1, 1],
        "6":[1, 1, 0, 0, 1, 1, 0, 1, 1],
        "7":[1, 0, 0, 1, 0, 0, 0, 1, 0],
        "8":[1, 1, 0, 1, 1, 1, 0, 1, 1],
        "9":[1, 1, 0, 1, 1, 0, 0, 1, 1],
        "0":[1, 1, 0, 1, 0, 1, 0, 1, 1]}
    for i in x[j]:
        numberX(d.get(i), a)
    

    


tr.exitonclick()


        


