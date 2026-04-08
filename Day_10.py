import turtle as t
from turtle import Screen

numOfSides = 3
deg = 360 / numOfSides
for _ in range(50):
    t.forward(50)
    t.right(deg)
    numOfSides += 1

t.exitonclick()
