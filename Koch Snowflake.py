# Draw a Koch snowflake - a fractal shape


from ifm import *
from math import cos,sin,pi,radians

global curr_x
global curr_y
global currang


def line_at_angle(leng):

  global curr_x
  global curr_y
  global currang
  new_x = curr_x + int(leng*cos(radians(currang)))
  new_y = curr_y + int(leng*sin(radians(currang)))
  draw(new_x,new_y)
  curr_x = new_x
  curr_y = new_y
  
  
  

def koch_curve(iterations, length, shortening_factor, angle):

  global curr_x
  global curr_y
  global currang

  if iterations == 0:
    line_at_angle(length)
  else:
    iterations = iterations - 1
    length = int(length / shortening_factor)

    koch_curve(iterations, length, shortening_factor, angle)
    currang-=angle
    koch_curve(iterations, length, shortening_factor, angle)
    currang+=2*angle
    koch_curve(iterations, length, shortening_factor, angle)
    currang-=angle
    koch_curve(iterations, length, shortening_factor, angle)





filename = "snow.svg"
start(filename)

page_size(900,900)
line_col('black')
fill_col('yellow')
line_width(2)


curr_x = 180
curr_y = 288
currang = 0

start_path(curr_x,curr_y)

for i in range(3):  
  koch_curve(4, 600, 3, 60)
  currang+=120


end_closed_path()




finish()
display()




