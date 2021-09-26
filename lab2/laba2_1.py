import turtle as tr
import random as rn

tr.shape('arrow')
tr.speed(0)
tr.down()
tr.color("blue")
for i in range(1000):
    tr.right(rn.random()*360)
    tr.forward(rn.random()*50)

