# Paths - open and closed


from ifm import *
filename = "path1.svg"
start(filename)

line_width(2)
page_size(600,400)

line_col('#0000FF')
fill_col('none')

# open path
start_path(50,100)
draw(250,100)
draw(250,150)
move(250,200)
draw(50,250)
end_path()


line_col('#00FF00')
# closed path
start_path(300,100)
draw(500,100)
move(500,150)
draw(500,200)
draw(300,250)
end_closed_path()



finish()
display()







