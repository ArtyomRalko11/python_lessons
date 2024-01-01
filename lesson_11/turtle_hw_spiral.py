from turtle import *


t = Turtle()
t.speed(0)

angle = int(input('Enter the number of angles: '))
length = 100
for i in range(36):
    t.fd(length)
    t.lt(360 // angle)
    length += 4


done()