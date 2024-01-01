import math
import random as r
import string as s
from turtle import *

t = Turtle()
t.speed(0)

radius = 5
angle = 5
turns = 500
colors = []
alphabet = s.hexdigits


for i in range(360):
    color = '#'
    for j in range(6):
        color += r.choice(alphabet)
    colors.append(color)

for i in range(turns * 360 // angle):
    t.color(r.choice(colors))
    t.fd(angle * math.pi / 180 * radius)
    t.lt(angle)
    radius += 0.1
    angle += 0.001



t.hideturtle()
done()