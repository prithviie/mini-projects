import turtle
import time
import random

delay = 0.1

# score
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head 
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("yellow")
food.penup()
food.goto(0, 100)

# for snake body
segments = []

# pen - for score
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.color('white')
pen.goto(0, 260)
pen.write("Score: 0    High score: 0", align="center", font=("Courier", 24, "normal"))


# functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# main game loop
while True:
    wn.update()

    # check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # clear segments lists
        segments.clear()

        # reset score to 0
        score = 0
        pen.clear()
        pen.write("Score: {}    High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # reset the delay
        delay = 0.1

    # check for food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape('square')
        segment.color('grey')
        segment.penup()

        segments.append(segment)

        # reduce delay
        delay -= 0.001

        # increase score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}    High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # move the end segment first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for body collisions
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # clear segments lists
            segments.clear()

            # reset score to 0
            score = 0
            pen.clear()
            pen.write("Score: {}    High score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            # reset the delay
            delay = 0.1


    time.sleep(delay)


wn.mainloop()