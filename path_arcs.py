# This is a program showing arcs of circles and ellipses

from ifm import *

filename = "path_arcs.svg"
start(filename)
    
page_size(400,300)

line_col('#000000')         # line colour black
fill_col('none')

line_width(2)               # line width = 2px


# Arcs of circles

rx=60
ry=60

x=120
y1=30
y2=130

type=1
line_col('red')         # line colour red
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

type=2
line_col('green')         # line colour green
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

type=3
line_col('blue')         # line colour blue
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

type=4
line_col('yellow')         # line colour yellow
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()



# Arcs of ellipses

rx=70
ry=50

x=270
y1=175
y2=250

type=1
line_col('red')         # line colour red
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

type=2
line_col('green')         # line colour green
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

type=3
line_col('blue')         # line colour blue
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

type=4
line_col('yellow')         # line colour yellow
start_path(x,y1)
path_arc(rx,ry,type,x,y2)
end_path()

finish()
display()



