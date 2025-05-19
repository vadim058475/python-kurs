import turtle
import time


window = turtle.Screen()
window.bgcolor("white")


square = turtle.Turtle()
square.shape("square")
square.shapesize(5, 5)
square.penup()


colors = ["red", "green"]


for i in range(5):
    for color in colors:
        square.color(color)
        time.sleep(1)








