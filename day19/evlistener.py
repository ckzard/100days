from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("DeepPink")

screen.listen()

def move_forwards():
    tim.forward(10)

def move_left():
    # tim.left(30)
    new_heading = tim.heading() + 30
    tim.setheading(new_heading)

def move_right():
    # tim.right(30)
    new_heading = tim.heading() - 30
    tim.setheading(new_heading)

def move_back():
    tim.back(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# screen.onkeypress(move_forwards, 'space')
screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_right, 'd')
screen.onkeypress(move_left, 'a')
screen.onkeypress(move_back, 's')
screen.onkeypress(clear, 'c')



screen.exitonclick()