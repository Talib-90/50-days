import turtle 

# Program 1
screen = turtle.Screen()
screen.title("My first turtle")
screen.bgcolor("black")

t = turtle.Turtle()
t.color("yellow")
t.pensize(2)

t.begin_fill()
t.circle(80)
t.end_fill()


t2 = turtle.Turtle()
t2.color("white")
t2.pensize(2)

t2.penup()
t2.goto(-50, -50)
t2.pendown()

for _ in range(2):
    t2.forward(100)
    t2.left(90)
    t2.forward(30)
    t2.left(90)



# Program 2

screen = turtle.Screen()
t = turtle.Turtle()

screen.title("Triangle")
t.color("blue")
t.penup()
t.pensize(5)
t.goto(-100, -170)
t.pendown()
t.fillcolor("blue")
t.begin_fill()

for _ in range(3):
    t.forward(200)
    t.left(120)

t.end_fill()

turtle.done()