from turtle import Turtle, Screen
import random

is_gameOn = False
window = Screen()
window.setup(width=500, height=400)
user_input = window.textinput(title="Make your bet", prompt="Which turtle win the race? Choose a color: ")
colors = ["red", "yellow", "purple", "green", "blue", "orange"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for t_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[t_index])
    all_turtles.append(new_turtle)

if user_input:
    is_gameOn = True

while is_gameOn:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_gameOn = False
            winningColor = turtles.pencolor()
            if winningColor == user_input:
                print(f"You've won! The {winningColor} turtles is the winner!.")
            else:
                print(f"You've lose! The {winningColor} turtles is the winner!.")

        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

# def move_forward():
#     return tim.forward(10)

# def move_backward():
#     return tim.backward(10)

# def move_left():
#     # heading = tim.heading() + 10
#     # return tim.setheading(heading)
#     return tim.left(10)

# def move_right():
#     # heading = tim.heading() - 10
#     # return tim.setheading(heading)
#     return tim.right(10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# window.listen()
# window.onkey(move_forward, "w")
# window.onkey(move_backward, "s")
# window.onkey(move_left, "a")
# window.onkey(move_right, "d")
# window.onkey(clear, "c")
window.exitonclick()
