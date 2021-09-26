import numpy as np
import turtle as tr
import random as rn
import pathlib


def move():
    tr.forward(SIZE)
    return
def left():
    tr.left(ANGLE)
    return
def right():
    tr.right(ANGLE)
    return
def top():
    return
def movedop():
    tr.forward(SIZE)
    return

def do_actions(s):
    for a in s:
        if a in actions:
            actions[a]()
    return

def juide(s):
    ns=''
    for r in s:
        if r in rules:
            ns +=rules[r]
        else:
            ns+=r
    return ns

def resettr():
    tr.clear()
    tr.up()
    tr.goto(x0,y0)
    tr.seth(0)
    return


Nomer=int(input())*9
inp = open(pathlib.Path("infa_2021_samodelkin", "lab2", "input_Lsys_2.txt"), 'r')
for i in range(Nomer):
    inp.readline()
inp.readline()
x0=int(inp.readline())
y0=int(inp.readline())
rulkeys=list(inp.readline().split("=!!="))
rulval=list(inp.readline().split("=!!="))
s=inp.readline()
SIZE= int(inp.readline())
ANGLE=int(inp.readline())
kolvo=int(inp.readline())

rules={rulkeys[i].rstrip():rulval[i].rstrip() for i in range(len(rulkeys))}
actions={
    't': movedop,
    'm': top,
    'f': move,
    '+': left,
    '-': right
}
tr.shape('arrow')
tr.speed(0)
tr.tracer(False)
for i in range(kolvo):
    resettr()
    tr.down()
    s=juide(s)
do_actions(s)
tr.tracer(True)
inp.close()
tr.exitonclick()