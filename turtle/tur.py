# Случайное движение черепашки

import turtle
import os
from random import random

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

t.setpos(0, 0)
t.left(90)
t.color("green")
k = 0
while (k < 5):
    t.down()
    r = random() * 10
    c = random()
    if c <= 0.5:
        t.right(r)
    else:
        t.left(r)
    t.forward(1)
    os.system('clear')
    print("X: ", round(t.xcor(), 1))
    print("Y: ", round(t.ycor(), 1))
    if (t.xcor() > 300 or
       t.xcor() < -300 or
       t.ycor() > 300 or
       t.ycor() < -300):
        t.up()
        t.setpos(0, 0)
        t.seth(random() * 360)
        k = k + 1

turtle.done()
