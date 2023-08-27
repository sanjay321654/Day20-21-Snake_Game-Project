from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

coordinates = [(0, 0), (-20, 0), (-40, 0)]
all_segments = []
screen.tracer(0)
for position in coordinates:
    tom = Turtle("square")
    tom.color("white")
    tom.penup()
    tom.goto(position)
    all_segments.append(tom)

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(all_segments) - 1, 0, -1):
        new_x = all_segments[seg - 1].xcor()
        new_y = all_segments[seg - 1].ycor()
        all_segments[seg].goto(new_x, new_y)

    all_segments[0].forward(20)
    all_segments[0].left(90)

screen.exitonclick()
