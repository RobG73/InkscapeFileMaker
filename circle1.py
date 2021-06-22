# This is a program to create a circle and ellipse

from ifm import *
filename = "circ1.svg"
start(filename)

units("cm")

line_width(0.2)
page("A4",1)

line_col('#FF0000')
fill_col('#FFFF00')
circle(8,10,6)

line_col('#0000FF')
fill_col('#00FFFF')
ellipse(21,10,7,5)

finish()
display()




# Explanation

#  from ifm import *       <- import the ifm library
#  filename = "circ1.svg"  <- choose the name of the file to create
#  start(filename)         <- then start making it
#  units("cm")             <- use "cm" as units in program
#  line_width(0.2)         <- Choose a line-width of .2cm 
#  page("A4", 1)           <- Choose the page size - here A4 landscape

#  line_col('#FF0000')     <- Choose a line colour, here we choose red
#  fill_col('#FFFF00')     <- Choose a fill colour, here we choose yellow
#  circle(8,10,6)          <- circle, centre at (8cm,10cm), radius 6cm

#  line_col('#0000FF')     <- Change line colour to blue
#  fill_col('#00FFFF')     <- Change fill colour to cyan
#  ellipse(21,10,7,5)      <- Ellipse, cente at (21cm,10cm), x-radius=7cm, y-radius=5cm

#  finish()                <- finish the file
#  display()               <- automatically open and display the file (windows only)








