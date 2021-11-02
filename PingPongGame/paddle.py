from turtle import Screen, Turtle

class Paddle(Turtle):  # inheriting from Turtle class
    def __init__(self, postion):
        super(Paddle, self).__init__()   # used for inheriting all the values
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(postion)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


