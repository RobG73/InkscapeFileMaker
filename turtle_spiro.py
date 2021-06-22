
#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/

import turtle
from math import cos,sin,pi
from time import sleep

def get_rots(nR,nr):
    # Calculate number of rotations of
    # inner circle around large circle
    n=1
    while n*nR/nr!=int(n*nR/nr):
        n+=1
    return n

window = turtle.Screen()
window.bgcolor("#FFFFFF")

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
myPen.pensize(1)
myPen.color("#FF0000")

R = 206   # large circle radius
r = 78    # inner circle radius
d = 55    # distance of pen from centre of inner circle

rotations = get_rots(R,r)

angle = 0

myPen.penup()
myPen.goto(R-r+d,0)
myPen.pendown()

theta = pi/30
steps = 60*rotations

for t in range(0,steps+1):
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    myPen.goto(x,y)
    angle+=theta    





