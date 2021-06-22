# This is a program to create a grid of 1 cm squares
# on an A4 sheet in portrait mode.

from ifm import *
filename = "grid1.svg"
start(filename)

units("cm")

line_width(0.02)
page("A4")

line_col('#0000DD')
fill_col('none')

top_margin = 2.0   # top margin = 2 cm
left_margin = 2.0  # left margin = 2 cm
noc = 17           # number of columns
nor = 26           # number of rows


# Draw vertical lines
y1 = top_margin
y2 = y1 + nor*1
for a in range(noc+1):
    x = left_margin + a*1
    line(x,y1,x,y2)

#Draw horizontal lines
x1 = left_margin
x2 = x1 + noc*1
for b in range(nor+1):
    y = top_margin + b*1
    line(x1,y,x2,y)

finish()
display()







