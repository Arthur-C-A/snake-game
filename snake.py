from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def moving_snake(self):

        for pos in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[pos - 1].xcor()
            ycor = self.segments[pos - 1].ycor()
            self.segments[pos].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)



    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def reset(self):
        for turtle in self.segments:
            turtle.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def add_tail(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)