import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
"""
segment_1 = Turtle(shape="square")
segment_1.color("white")

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20, 0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-40, 0)
this part made the for loops isues
"""

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)

    segments[0].left(90)





screen.exitonclick()