import turtle as t
from turtle import Screen

numOfSides = 3
deg = 360 / numOfSides
for _ in range(50):
    tim = t.forward(50)
    tim = t.right(deg)
    numOfSides += 1
    
t.exitonclick()