from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score
tom = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
bg_image_path = "snakebg.gif"
tom.bgpic(bg_image_path)
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the collision with the food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_card()

    # Detect the collision on the wall.
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or
            snake.head.ycor() < -290):
        game_on = False
        score.game_over_words()

    # detect collision with tail.
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over_words()


screen.exitonclick()
