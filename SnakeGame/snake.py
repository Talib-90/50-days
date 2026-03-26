from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.createSnake()
        self.head = self.segment[0]
    
    def createSnake(self):
        for position in STARTING_POSITION:
            self.addSegment(position)

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segment.append(newSegment)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.createSnake()
        self.head = self.segment[0]

    def extendSegment(self):
        self.addSegment(self.segment[-1].position())

    def move(self):
        for new_seg in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[new_seg - 1].xcor()
            y_cor = self.segment[new_seg - 1].ycor()
            self.segment[new_seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
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