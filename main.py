import turtle
from time import sleep
from random import randint

delay = 0.1
score = 0
high_score = 0

# info
def info():
    pen.clear()
    pen.color("white")
    pen.goto(0, 250)
    pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

# gameover
def gameover():
    pen.color("#FF0000")
    pen.goto(0, 0)
    head.direction = "Stop"
    pen.write("GAME OVER", align="center", font=("montserrat", 30, "bold"))
    wn.update()
    sleep(3)
    for segment in segments:
        segment.goto(1000, 1000)
    head.goto(0, 0)
    segments.clear()
    score = 0
    delay = 0.1
    pen.clear()

# creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#2F4F4F")
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("#7FFFD4")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('#FFD700')
food.penup()
food.goto(0, 100)

# appears informations at screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0  High Score: 0", align="center", font=("candara", 24, "bold"))

# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")


segments = []

# main gameplay
while True:
    wn.update()
    # checking for head hits the window limit
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        sleep(0.3)
        gameover()
        score = 0
        delay = 0.1
        info()
    if head.distance(food) < 20:
        x = randint(-270, 270)
        y = randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#53cbbf") #tail color
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score: {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    # checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y) 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            sleep(0.3)
            gameover()
            score = 0
            delay = 0.1
            info()
    sleep(delay)

wn.mainloop()