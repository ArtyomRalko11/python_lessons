from turtle import *

# Create a turtle for drawing
flower = Turtle()
flower.color("blue")
flower.speed(2)

# Draw the flower petals
for petal in range(6):
    flower.fd(100)
    flower.rt(45)
    flower.fd(100)
    flower.rt(135)
    flower.fd(100)
    flower.rt(45)
    flower.fd(100)
    flower.rt(135)

    # Offset for the next petal
    flower.rt(60)

# Draw the flower center
flower.color("yellow")
flower.dot(30)

done()