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
water.shapesize(stretch_wid=5, stretch_len=2)

#fire
fire = turtle.Turtle()
fire.speed(0)
fire.shape("square")
fire.color("red")
fire.penup()
fire.goto(350, 0)
fire.shapesize(stretch_wid=5, stretch_len=2)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#functions
def water_up():
    y = water.ycor()
    y += 20
    water.sety(y)


def water_down():
    y = water.ycor()
    y -= 20
    water.sety(y)


def fire_up():
    y = fire.ycor()
    y += 20
    fire.sety(y)

def fire_down():
    y = fire.ycor()
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
