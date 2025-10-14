# Turtle Graphics: Spiral Circle Pattern

# This Python turtle program draws an artistic pattern made up of repeating arcs
# and rotations using concentric circles. Here's how it works:

# - The background color is set to a dark blue (`#274295`) and the pen color is initially gray (`#535466`).
# - A list of 4 color shades (`col`) is used to change the pen color for variation.
# - The outer loop (`range(10)`) gradually increases the radius of the circle with each iteration.
# - The inner loop (`range(20)`) draws a quarter-circle twice to form square-like arcs.
# - After each arc set, the turtle turns left by 45° to rotate the pattern.
# - Pen color changes every outer iteration to give a multicolor spiral effect.
# The result is a complex, hypnotic pattern of rotating circular arcs in beautiful earth tones.

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#274295')
t.pencolor('#535466')
t.speed(100)
col=('#ED7864', '#6E544F', '#592F2F', '#6E382E')

for index in range(10):
    for second_index in range(20):
        t.speed(5)
        for x in range(2):
            t.pensize(2)
            t.circle(80 + index * 20, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[index % 4])
s.exitonclick()
