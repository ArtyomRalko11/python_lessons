from turtle import *


t = Turtle()
t.speed(0)
t.color('red')

l = 100

for i in range(5):
    t.fd(l)
    t.lt(144)

t.up()
t.goto(50, -40)
t.down()
t.circle(55, 360)

done()