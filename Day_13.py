import turtle as t
from turtle import Screen
import random

# tim = t.Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)

# Challenge _1
# for _ in range(4):
#     t.right(90)
#     t.forward(100)

# Challenge _2
# for _ in range(15):
#     tim = t.forward(10)
#     tim = t.penup()
#     tim = t.forward(10)
#     tim = t.pendown()

# Challenge _3
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
direction = [0, 90, 180, 270]
# t.pensize(10)
# t.speed("fastest")
t.colormode(255)


# def drawShape(numOfSides):
#     deg = 360 / numOfSides
#     for _ in range(numOfSides):
#         tim = t.forward(50)
#         tim = t.right(deg)

# for shape in range(3,11):
#     t.color(random.choice(colours))
#     drawShape(shape)


# for _ in range(100):
#     t.color(random.choice(colours))
#     t.forward(30)
#     t.setheading(random.choice(direction))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


# for _ in range(100):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(direction))

# def spirograph(size):
#     for _ in range(int(360 / size)):
#         t.color(random_color())
#         t.circle(100)
#         t.setheading(t.heading() + size)

# spirograph(5)

# def spirograph(size):
#     for _ in range(int(360 / size)):
#         t.color(random_color())
#         t.circle(100)
#         t.setheading(t.heading() + size)

# spirograph(5)


t.penup()
t.home()
t.pendown()

t.setheading(0)
t.forward(100)

t.penup()
t.home()
t.pendown()

t.setheading(90)
t.forward(100)

t.penup()
t.home()
t.pendown()

t.setheading(180)
t.forward(100)

t.penup()
t.home()
t.pendown()

t.setheading(270)
t.forward(100)

t.exitonclick()
