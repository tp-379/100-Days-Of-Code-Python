# Day18 of my 100DaysOfCode Challenge
# Draw a different shapes using Turtle Graphics

from turtle import Turtle, Screen
import random

groot = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        groot.forward(100)
        groot.right(angle)


for shape_side_n in range(3, 10):
    groot.color(random.choice(colours))
    draw_shape(shape_side_n)


my_screen = Screen()
my_screen.exitonclick()
