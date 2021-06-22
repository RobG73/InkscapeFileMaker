

# Draw a table

# Note that you have to install numpy before running this program
# Go to command prompt (in folder, press shift and right click mouse
# select "Open command window here";
# Type in command: pip install numpy


from ifm import *
import numpy as np


# Data to be put into table
contents = np.array([
["Month", "Units", "Cost(ukp)"], 
[1, 56, 30.75],
[2, 64, 40.95],
[3, 71, 48.75],
[4, 81, 56.35],
[5, 92, 67.25],
[6, 93, 63.75],
[7, 96, 64.65],
[8, 99, 67.35],
[9, 91, 61.15],
[10, 85, 52.75],
[11, 73, 46.85],
[12, 59, 35.55]
])


dmon = ["Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]



filename = "table1.svg"
start(filename)
# line_width(2)
units('cm')

page("A4")
line_col('black')
fill_col('none',0)

noc=3   # Number of columns
nor=13   # Number of rows
woc=3.6  # width of columns
hor=2.0  # height of rows
lm=0.5*(21-noc*woc)  # left margin
tm=2.0     # top margin
cell_tm = 1.2 # Inside cell top margin 
cell_lm = 0.5*woc # Inside cell left margin 

line_width1 = 0.04
line_width2 = 0.1

line_width(line_width1)


y1 = tm
y2 = tm + nor*hor
for a in range(noc+1):
    x = lm + a*woc
    line(x,y1,x,y2)

x1 = lm
x2 = lm + noc*woc
for b in range(nor):
    if b==1:
        line_width(line_width2)
    else:
        line_width(line_width1)
    y = tm + b*hor
    # line(x1,y,x2,y)
    if b%2==1:
        fill_col('#00ddff',0.4)
    else:
        fill_col('none')
    rect(x1,y,noc*woc,hor)
    


    

line_width(line_width2)
rect(lm,tm,noc*woc,nor*hor)



line_width(0)
fill_col('black')
# font("Times New Roman",20)
font_desc("TNn",20)

num_cells = noc*nor

for i in range(num_cells):
    ix = i%noc
    iy = int(i/noc)
    xpos = lm + cell_lm + ix*woc
    ypos = tm + cell_tm + iy*hor
    t = contents[iy][ix]
    if iy==0:
        font_desc("TBn",20)
        pt=t
    else:
        font_desc("TNn",20)
        pt=str(t)
    if ix==0 and iy>0:
        nt = int(t)
        pt = dmon[nt-1]
    middle_print(pt,xpos,ypos)
        




finish()
display()

