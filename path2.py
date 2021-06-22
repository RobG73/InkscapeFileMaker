# Using absolute and relative coordinates in paths

from ifm import *
filename = "path2.svg"
start(filename)

line_width(2)
page_size(600,400)

line_col('#0000FF')
fill_col('none')

# absolute coordinates
start_path(50,100)
draw(250,100)
draw(250,200)
draw(50,250)
draw(50,100)
move(100,120)
draw(200,120)
draw(200,170)
draw(100,170)
draw(100,120)
end_path()

# relative coordinates
line_col('#FF0000')
start_path(300,100)
path_relative()
draw(200,0)
draw(0,100)
draw(-200,50)
draw(0,-150)
move(50,20)
draw(100,0)
draw(0,50)
draw(-100,0)
draw(0,-50)
end_path()



finish()
display()







