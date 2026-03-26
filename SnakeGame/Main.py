from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Score
import time

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("My snake game")
window.tracer(0)

snake = Snake()
food = Food()
score = Score()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    window.update()
    time.sleep(0.1)
    snake.move()

    # Collision
    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extendSegment()
        score.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        # is_game_on = False
        # score.game_over()
        snake.reset()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.reset()
            snake.reset()


window.exitonclick()