# This is a program to create a rectangle
# with width 150 pixels and height 100 pixels
# Cyan fill colour, and blue border


from ifm import *
filename = "rect1.svg"
start(filename)

line_width(2)
page_size(400, 300)
line_col('#0000FF')
fill_col('#00FFFF')

x = 50
y = 40
width = 150
height = 100
rect(x,y,width,height)

finish()
display()




# Explanation

#  from ifm import *       <- import the ifm library
#  filename = "rect1.svg"  <- choose the name of the file to create
#  start(filename)         <- then start making it
#  line_width(2)           <- Choose a line-width of 2 pixels - try changing this
#  page_size(400, 300)     <- Choose the page size - here 400 px width and 300px height
#  line_col('#0000FF')     <- Choose a line colour, here we choose Blue
#  fill_col('#00FFFF')     <- Choose a fill colour, here we choose green
#  x = 50                  <- Choose the x position of the top left corner
#  y = 40                  <- Choose the y position of the top left corner
#  width = 150             <- Choose the width of the rectangle
#  height = 100            <- Choose the height of the rectangle
#  rect(x,y,width,height)  <- Draw the rectangle
#  # rect(50,40,150,100)   <- or you can put it in a short command like this
#  finish()                <- finish the file
#  display()               <- automatically open and display the file (windows only)








