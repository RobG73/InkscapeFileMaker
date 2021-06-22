# This is a program to create a rectangle
# with width 150 pixels and height 100 pixels
# green fill colour, and blue partly transparent border


from ifm import *
filename = "rect1.svg"
start(filename)

line_width(8)
page_size(400, 300)
line_col('#0000FF', 0.5)
fill_col('#00FF00')

x = 50
y = 40
width = 150
height = 100
rect(x,y,width,height)

finish()
display()



# Note that in Inkscape, the border of the rectangle is drawn
# with half its thickness outside the rectangle, and half inside.
# Click on the rectangle in Inkscape - look at the dimensions
# boxes at the top.
# Half the border thickness (line_width) is 4px
# The x position is 50 - 4 px = 46px
# The y position is 40 - 4 px = 36px
# The width is 4 + 150 + 4 = 158px
# The height is 4 + 100 + 4 = 108px



# Explanation

#  from ifm import *       <- import the ifm library
#  filename = "rect1.svg"  <- choose the name of the file to create
#  start(filename)         <- then start making it
#  line_width(8)           <- Choose a line-width of 8 pixels - try changing this
#  page_size(400, 300)     <- Choose the page size - here 400 px width and 300px height
#  line_col('#0000FF', 0.5)<- Choose line colour Blue, opacity 0.5
#  fill_col('#00FF00')     <- Choose a fill colour, here we choose green
#  x = 50                  <- Choose the x position of the top left corner
#  y = 40                  <- Choose the y position of the top left corner
#  width = 150             <- Choose the width of the rectangle
#  height = 100            <- Choose the height of the rectangle
#  rect(x,y,width,height)  <- Draw the rectangle
#  # rect(50,40,150,100)   <- or you can put it in a short command like this
#  finish()                <- finish the file
#  display()               <- automatically open and display the file (windows only)








