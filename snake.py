from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]

MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_segments = []
        self.move_snake()

    def move_snake(self):
        for position in COORDINATES:
            tom = Turtle("square")
            tom.color("white")
            tom.penup()
            tom.goto(position)
            self.all_segments.append(tom)

    def move(self):

        for seg in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(new_x, new_y)

        self.all_segments[0].forward(MOVE_FORWARD)

    def Up(self):

        self.all_segments[0].setheading(UP)

    def down(self):
        self.all_segments[0].setheading(DOWN)

    def left(self):
        self.all_segments[0].setheading(LEFT)

    def right(self):
        self.all_segments[0].setheading(RIGHT)
