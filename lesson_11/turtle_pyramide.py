from turtle import *


t = Turtle()
t.speed(0)
t.pensize(5)
t.shape('turtle')
length = 2

y = 0
x = 0

for i in range(13):
    t.fd(length)
    t.bk(length * 2)
    length += 5
    y -= 10
    t.up()
    t.goto(x, y)
    t.down()

t.hideturtle()
done()