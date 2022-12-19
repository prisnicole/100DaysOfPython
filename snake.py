import time
from turtle import Turtle, Screen

DELAY = 0.1
'''
Notes: 
Screen is a singleton - i.e. you'll get back
the same object even if you create it multiple times 
'''
# Screen set up
snake_screen = Screen()
snake_screen.title("Snake")
snake_screen.bgcolor("black")
snake_screen.setup(300, 300)
snake_screen.tracer(0)

# Snake set up
snake = Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 100)
snake.direction = "stop"


# Snake Functions
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.sety(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# snake moves from head - cannot go l from r, vv; u from d vv;
def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


# event listener
snake_screen.listen()
snake_screen.onkey(go_up, "w")
snake_screen.onkey(go_down, "s")
snake_screen.onkey(go_right, "d")
snake_screen.onkey(go_left, "a")

while True:
    snake_screen.update()
    move()
    time.sleep(DELAY)
