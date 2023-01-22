import random
import turtle
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)
palette = colorgram.extract("maldives.jpeg",20)
rgb_colors = []
for color in palette:
    rgb_colors.append(color.rgb)

newcolors = []
for rgb in rgb_colors:
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    newcolors.append((r,g,b))

print(newcolors)

t = Turtle()
t.speed("fast")
t.penup()
t.hideturtle()
t.setheading(223)
t.forward(360)


t.setheading(360)
t.dot(30,random.choice(newcolors))
for _ in range(0,6):
    t.dot(30,random.choice(newcolors))
    t.forward(100)
    t.dot(30,random.choice(newcolors))
    for _ in range(0,4):
        t.forward(100)
        t.dot(30,random.choice(newcolors))

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(90)
    t.forward(50)
    t.setheading(360)

screen = Screen()
screen.exitonclick()

