from turtle import *


t = Turtle()
t.speed(0)
t.shape('turtle')


for i in range(36):
    t.circle(20)
    t.up()
    t.fd(37)
    t.down()
    t.rt(10)

done()