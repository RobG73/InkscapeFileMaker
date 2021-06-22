# This is a program showing arcs of circles and ellipses
# and sectors of circles and ellipses

from ifm import *

filename = "arcs.svg"
start(filename)
    
page_size(800,750)

line_col('#000000')         # line colour black
fill_col('none')

line_width(2)               # line width = 2px


# Arcs of circles

rx=60
ry=60

y=150
x1=130
x2=280
x3=430
x4=580

f=0.1


line_col('red',f)
ellipse(x1,y,rx,ry)
line_col('red')         # line colour red
arc(x1,y,rx,ry,0,90)

line_col('green',f)
ellipse(x2,y,rx,ry)
line_col('green')         # line colour green
arc(x2,y,rx,ry,30,90)

line_col('blue',f)
ellipse(x3,y,rx,ry)
line_col('blue')         # line colour blue
arc(x3,y,rx,ry,30,270)

line_col('yellow',f)
ellipse(x4,y,rx,ry)
line_col('yellow')         # line colour yellow
arc(x4,y,rx,ry,90,30)



# Sectors of circles
y =300

fill_col('none')
line_col('red',f)
ellipse(x1,y,rx,ry)
line_col('black')
fill_col('red')
sector(x1,y,rx,ry,0,90)

fill_col('none')
line_col('green',f)
ellipse(x2,y,rx,ry)
line_col('black')       
fill_col('green')
sector(x2,y,rx,ry,30,90)

fill_col('none')
line_col('blue',f)
ellipse(x3,y,rx,ry)
line_col('black')         
fill_col('blue')
sector(x3,y,rx,ry,30,270)


fill_col('none')
line_col('yellow',f)
ellipse(x4,y,rx,ry)
line_col('black')         
fill_col('yellow')
sector(x4,y,rx,ry,90,30)



fill_col('none')

# Arcs of ellipses

rx=70
ry=50
y=450


line_col('red',f)
ellipse(x1,y,rx,ry)
line_col('red')         # line colour red
arc(x1,y,rx,ry,0,90)


line_col('green',f)
ellipse(x2,y,rx,ry)
line_col('green')         # line colour green
arc(x2,y,rx,ry,30,90)


line_col('blue',f)
ellipse(x3,y,rx,ry)
line_col('blue')         # line colour blue
arc(x3,y,rx,ry,30,270)


line_col('yellow',f)
ellipse(x4,y,rx,ry)
line_col('yellow')         # line colour yellow
arc(x4,y,rx,ry,90,30)


# Sectors of ellipses
y =600


line_col('red',f)
ellipse(x1,y,rx,ry)
line_col('black')        
fill_col('red')
sector(x1,y,rx,ry,0,90)

fill_col('none')
line_col('green',f)
ellipse(x2,y,rx,ry)
line_col('black')        
fill_col('green')
sector(x2,y,rx,ry,30,90)


fill_col('none')
line_col('blue',f)
ellipse(x3,y,rx,ry)
line_col('black')        
fill_col('blue') 
sector(x3,y,rx,ry,30,270)


fill_col('none')
line_col('yellow',f)
ellipse(x4,y,rx,ry)
line_col('black')        
fill_col('yellow') 
sector(x4,y,rx,ry,90,30)


line_width(0)
fill_col('black')
font_desc("TNn",16)
middle_print('0-90',x1,50)
middle_print('30-90',x2,50)
middle_print('30-270',x3,50)
middle_print('90-30',x4,50)


finish()
display()



