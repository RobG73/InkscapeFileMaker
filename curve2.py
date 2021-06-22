# This is a program showing cubic bezier curves

from ifm import *

filename = "curve2.svg"
start(filename)
    
page_size(400,300)

line_col('#000000')         # line colour black
fill_col('none')

line_width(1)               # line width = 1px


y1=50
yc1=100
yc2=200
y3=250

# Note that circles have been drawn to show the location of the control points
# These would, of course, not normally be drawn.


line_col('#FF0000')            # line colour red
x=50
xc1=x+20                       # control point 20px away from line
xc2=x+20                       # control point 20px away from line
start_path(x,y1)
curve2(xc1,yc1,xc2,yc2,x,y3)
end_path()
circle(xc1,yc1,1)             # location of control point 1
circle(xc2,yc2,1)             # location of control point 2


line_col('#00FF00')           # line colour green
x=100
xc1=x+60                      # control point 60px away from line
xc2=x+60                      # control point 60px away from line
start_path(x,y1)
curve2(xc1,yc1,xc2,yc2,x,y3)
end_path()
circle(xc1,yc1,1)             # location of control point 1
circle(xc2,yc2,1)             # location of control point 2


line_col('#0000FF')           # line colour blue
x=200
xc1=x-20                      # control point 20px away left of line
xc2=x+40                      # control point 40px away right of line
start_path(x,y1)
curve2(xc1,yc1,xc2,yc2,x,y3)
end_path()
circle(xc1,yc1,1)             # location of control point 1
circle(xc2,yc2,1)             # location of control point 2


line_col('#000000')           # line colour black
x=300
xc1=x+40                      # control point 40px away right of line
xc2=x-40                      # control point 40px away left of line
start_path(x,y1)
curve2(xc1,yc1,xc2,yc2,x,y3)
end_path()
circle(xc1,yc1,1)             # location of control point 1
circle(xc2,yc2,1)             # location of control point 2


finish()
display()



