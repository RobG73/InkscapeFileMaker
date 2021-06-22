# This is a program to create a rectangle
# with curved corners and horizintal gradient fill

from ifm import *
filename = "rect2.svg"
start(filename)

units("mm")

line_width(2)
page("A4", 1)

line_col('#FF0000',0.5)
linear_gradient("blue","cyan",0,0.9,0.2)


x = 30
y = 40
width = 150
height = 100
radius = 10
rect(x,y,width,height,radius,radius)

finish()
display()




# Explanation

#  from ifm import *       <- import the ifm library
#  filename = "rect2.svg"  <- choose the name of the file to create
#  start(filename)         <- then start making it
#  units("mm")             <- use "mm" as units in program
#  line_width(2)           <- Choose a line-width of 2mm 
#  page("A4", 1)           <- Choose the page size - here A4 landscape
#  line_col('#FF0000',0.5) <- Choose a line colour, here we choose red, opacity 0.5
#  linear_gradient("blue","cyan",0,0.9,0.2)  -> the fill is a horizontal linear gradient
#                                            -> from blue (opacity 0.9) to cyan (opacity 0.2)
#  x = 30                  <- Choose the x position of the top left corner
#  y = 40                  <- Choose the y position of the top left corner
#  width = 150             <- Choose the width of the rectangle
#  height = 100            <- Choose the height of the rectangle
#  radius = 10             <- Choose the radius of the corners
#  rect(x,y,width,height,radius,radius)  <- Draw the rectangle
#  # rect(30,40,150,100,10,10)   <- or you can put it in a short command like this
#  finish()                <- finish the file
#  display()               <- automatically open and display the file (windows only)








