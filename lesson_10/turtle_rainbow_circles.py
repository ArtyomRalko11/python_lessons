import random as r
import string as s
from turtle import *

colors = []
alphabet = s.hexdigits
for i in range(100000):
    color = '#'
    for j in range(6):
        color += r.choice(alphabet)
    colors.append(color)
print(colors)
t = Turtle()
t.speed(9)

rounds = r.randint(400, 1500)
for circle in range(rounds):
    x = r.randint(-500, 500)
    y = r.randint(-500, 500)
    d = r.randint(100, 160)
    col = r.choice(colors)
    t.color(col)
    t.up()
    t.goto(x, y)
    t.down()
    t.dot(d)
done()