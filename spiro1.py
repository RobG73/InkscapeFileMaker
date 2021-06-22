
# Draw a spirograph pattern
# converted from version at:
# www.101computing.net/python-turtle-spirograph/


from ifm import *
from math import cos,sin,pi

def get_rots(nR,nr):
    # Calculate number of rotations of
    # inner circle around large circle
    n=1
    while n*nR/nr!=int(n*nR/nr):
        n+=1
    return n


filename = "spiro1.svg"
start(filename)

line_width(0)

page_size(600,600)
fill_col('black')

R = 205   # large circle radius
r = 75    # inner circle radius
d = 55    # distance from centre of inner circle

font_desc("TNn",20)
text_print("R = "+str(R),50,50)
text_print("r = "+str(r),50,90)
text_print("d = "+str(d),50,130)

rotations = get_rots(R,r)

line_width(2)
fill_col('none',0)

# centre of large circle
xc = 300
yc = 300

angle = 0

prevx = xc+R-r+d
prevy = yc
start_path(prevx,prevy)

theta = pi/30
steps = 60*rotations  # = 2*pi*rotations/theta

prev_p = 0

line_col('red')

for t in range(0,steps+1):   
    
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    xp = xc + x
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    yp = yc + y
    draw(xp,yp)  # draw the line
    angle+=theta
    p = int(angle/(2*pi))
    if p!=prev_p:
        # p = record progress - how many times inner circle
        # goes around outer circle
        print(p)  # delete this line if desired
        prev_p=p
    

end_path()

finish()
display()

