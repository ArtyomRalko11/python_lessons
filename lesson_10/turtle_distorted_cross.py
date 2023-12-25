from turtle import *

t = Turtle()
t.speed(0)

length = int(input('Enter length:'))
t.lt(90)
for i in range(3):
    t.rt(120)
    t.fd(length)
    t.rt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)



done()