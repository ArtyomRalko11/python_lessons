from turtle import *

# Create a turtle for drawing
house = Turtle()
house.shape('turtle')
house.color('#401d02')
house.speed(9)
house.pensize(7)
house.begin_fill()

# Drawing the outline of the house
for i in range(4):
    house.fd(299)
    house.rt(90)
house.end_fill()
house.lt(60)
house.begin_fill()

# Drawing the roof
for i in range(3):
    house.fd(299)
    house.rt(120)
house.end_fill()
house.pensize(4)
house.up()
print(house.pos())
house.goto(50, -50)
house.rt(60)
house.pensize(3)
house.down()
house.color('#000000')
house.begin_fill()

# Drawing the window
for i in range(4):
    house.fd(80)
    house.rt(90)
house.color('#5686ba')
house.end_fill()
house.color('#401d02')
house.up()
house.color('#000000')
house.begin_fill()
house.goto(190, -140)
house.down()

# Drawing the door
house.fd(80)
house.rt(90)
house.fd(110)
house.rt(90)
house.fd(80)
house.rt(90)
house.fd(110)
house.color('#7a4720')
house.end_fill()
house.color('#401d02')
house.up()
house.fd(30)

done()