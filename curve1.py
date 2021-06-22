# This is a program showing quadratic bezier curves

from ifm import *

filename = "curve1.svg"
start(filename)
    
page_size(300,200)

line_col('#000000')         # line colour black
fill_col('none')

line_width(1)               # line width = 2px


y1=50
yc=100
y3=150


line_col('#FF0000')         # line colour red
x=50
xc=x+20                     # control point 20px away from line
start_path(x,y1)
curve1(xc,yc,x,y3)
end_path()
circle(xc,yc,1)             # location of control point


line_col('#00FF00')         # line colour green
x=100
xc=x+40                     # control point 40px away from line
start_path(x,y1)
curve1(xc,yc,x,y3)
end_path()
circle(xc,yc,1)             # location of control point

line_col('#0000FF')         # line colour blue
x=150
xc=x+60                     # control point 60px away from line
start_path(x,y1)
curve1(xc,yc,x,y3)
end_path()
circle(xc,yc,1)             # location of control point

line_col('#000000')         # line colour black
x=200
xc=x+80                     # control point 80px away from line
start_path(x,y1)
curve1(xc,yc,x,y3)
end_path()
circle(xc,yc,1)             # location of control point


finish()
display()



