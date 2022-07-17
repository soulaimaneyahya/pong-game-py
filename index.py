#imported turtle module
import turtle

wind = turtle.Screen() # init screen object
wind.title("Ping Pong by Soulaimane Yahya")
wind.bgcolor("black")
wind.setup(width=800, height=600)
# for screen update
wind.tracer(0) # stop wind from updating auto

#water
water = turtle.Turtle()
water.speed(0)
water.shape("square")
water.color("blue")
water.penup()
water.goto(-350, 0)
water.shapesize(stretch_wid=5, stretch_len=1)

#fire
fire = turtle.Turtle()
fire.speed(0)
fire.shape("square")
fire.color("red")
fire.penup()
fire.goto(350, 0)
fire.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# delta, rate of change
ball.dx = 0.2
ball.dy = 0.2

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("water: {}    fire: {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))

#functions
def water_up():
    y = water.ycor()
    if water.ycor() < 250:
        y += 20
        water.sety(y)


def water_down():
    y = water.ycor()
    if water.ycor() > -250:
        y -= 20
        water.sety(y)


def fire_up():
    y = fire.ycor()
    if fire.ycor() < 250:
        y += 20
        fire.sety(y)

def fire_down():
    y = fire.ycor()
    if fire.ycor() > -250:
        y -= 20
        fire.sety(y)

# keyboard binding
wind.listen()
wind.onkeypress(water_up, "w")
wind.onkeypress(water_down, "s")
wind.onkeypress(fire_up, "Up")
wind.onkeypress(fire_down, "Down")

# main game loop
while True:
    wind.update() #updates the screen everytime the loop run
    # move th ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse dire

    if ball.xcor() > 390:
        ball.goto(0,0) # go to center
        score1 += 1
        ball.dx *= -1
        score.clear()
        score.write("water: {}    fire: {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        score2 += 1
        ball.goto(0,0)
        ball.dx *= -1
        score.clear()
        score.write("water: {}    fire: {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))


    # ball collision
    if (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() > fire.ycor() -50 and ball.ycor() < fire.ycor() + 40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() > water.ycor() -50 and water.ycor() < water.ycor() + 40):
        ball.setx(-330)
        ball.dx *= -1

