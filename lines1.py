# This is a program showing lines with arrows

from ifm import *
import random
import math

filename = "lines.svg"
start(filename)
    
page_size(400,200)

line_col('#000000')         # line colour black
fill_col('#000000')         # fill colour black

line_width(2)               # line width = 2px

x1=50
x2=200

line(x1,50,x2,50,4,0)       # start_arrow is 4x line width
                            # end_arrow is 0


line(x1,100,x2,100,0,5)     # start_arrow is 0
                            # end_arrow is 5x line width

                            
line(x1,150,x2,150,6,7)     # start_arrow is 6x line width
                            # end_arrow is 7x line width


line_width(1)               # change line width to 1 pixel

line(300,50,300,150,6,6)    # start_arrow is 6x line width
                            # end_arrow is 6x line width


line(320,50,360,180,0,6)    # start_arrow is 6x line width
                            # end_arrow is 6x line width


line_col('#000000')         # line colour black
fill_col('#FF0000')         # fill colour red

line(270,55,230,110,0,4)    # end_arrow = 4x line width


line_col('#00FF00')         # line colour green
fill_col('#00FF00')         # fill colour green

line(230,120,270,150,0,4)   # end_arrow = 4x line width

finish()
display()



