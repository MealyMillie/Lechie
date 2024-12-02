import turtle
import math

t = turtle.Turtle()
t.speed(1000)
t.color("hotpink")
turtle.bgcolor("beige")

def corazon(n):
    x = 25 * math.sin(n) ** 3
    y = 15 * math.cos(n) - 5 *\
     math.cos(2*n) - 2*math.cos(3*n) - \
     math.cos(4*n)
    return x, y

t.penup()
for i in range(15):
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 100, 2):
        x, y = corazon(n/10)
        t.goto(x*i, y*i)
    t.penup()

t.penup()
t.goto(10, -20)  
t.color("red")
t.write(
    "I LOVE YOU MY PUCCINO",
    align="center",
    font=("Georgia", 20, "bold")
)
t.hideturtle()

t.hideturtle()
turtle.done()


    