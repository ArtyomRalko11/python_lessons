from turtle import *


t = Turtle()
t.speed(0)
t.shape('turtle')

t.lt(90)
for i in range(4):
    t.circle(25, 180)
    t.rt(90)

done()