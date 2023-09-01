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
        self.head = self.all_segments[0]

    def move_snake(self):
        for position in COORDINATES:
            self.add_segments(position)

    def add_segments(self, position):
        tom = Turtle("square")
        tom.color("white")
        tom.penup()
        tom.goto(position)
        self.all_segments.append(tom)

    def extend(self):
        self.add_segments(self.all_segments[-1].position())


    def move(self):

        for seg in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(new_x, new_y)

        self.head.forward(MOVE_FORWARD)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)
