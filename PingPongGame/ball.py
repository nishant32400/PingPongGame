from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()  # self is the object of Turtle class
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        # print(f"new_y: {new_y} and y_cor: {self.y_cor}") # understanding
        self.goto(new_x, new_y)

    def bounce_y(self):  # detect collision with walls
        self.y_cor *= -1
        # print(f"After bounce y_cor:{self.y_cor}")   # understanding

    def bounce_x(self):  # detect collision with paddle
        self.x_cor *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



