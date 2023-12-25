from turtle import *


t = Turtle()
t.speed(0)
t.shape('turtle')

t.lt(90)
for i in range(7):
    t.circle(25, 180)
    t.rt(180)

t.up()
t.goto(-15, 0)
t.down()
for i in range(7):
    t.circle(25, -180)
    t.rt(180)

t.up()
t.goto(100, 99)
t.down()
for i in range(36):
    t.circle(10)
    t.up()
    t.fd(40)
    t.down()
    t.rt(10)

done()