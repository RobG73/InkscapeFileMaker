
# Draw a spirograph pattern
# www.101computing.net/python-turtle-spirograph/

# Added colour changes;
# Used line() commands instead of path commands
# because the whole of a path can only be one colour
# each of the "lines" can be different colours.

from ifm import *
from math import cos,sin,pi

def get_rots(nR,nr):
    # Calculate number of rotations of
    # inner circle around large circle
    n=1
    while n*nR/nr!=int(n*nR/nr):
        n+=1
    return n


filename = "spiro2.svg"
start(filename)



page_size(600,600)
line_col('black')
fill_col('black')
line_width(0)

R = 205   # large circle radius
r = 77    # inner circle radius
d = 55    # distance from centre of inner circle

font_desc("TNn",16)
text_print("R = "+str(R),50,50)
text_print("r = "+str(r),50,80)
text_print("d = "+str(d),50,110)



rotations = get_rots(R,r)
# print(rotations)

# Original values of red,green and blue
rcol = 0
gcol = 255
bcol = 128

# Directions in which colours change
# +1 = increase amount of that colour
# -1 = decrease amount of that colour
d_rcol = 1
d_gcol = -1
d_bcol = 1

# How much each of red, green and blue changes
# for each iteration of t
rcol_change = 3
gcol_change = 4
bcol_change = 5

rdir = " (+" if d_rcol == 1 else " (-"
gdir = " (+" if d_gcol == 1 else " (-"
bdir = " (+" if d_bcol == 1 else " (-"

rtext = "Red = "+str(rcol)+rdir+str(rcol_change)+")"
gtext = "Green = "+str(gcol)+gdir+str(gcol_change)+")"
btext = "Blue = "+str(bcol)+bdir+str(bcol_change)+")"

right_print(rtext,550,50)
right_print(gtext,550,80)
right_print(btext,550,110)



# centre of large circle
xc = 300
yc = 300

fill_col('none')
line_width(2)

angle = 0

# previous values of x and y
prevx = xc+R-r+d
prevy = yc

theta = pi/30
steps = 60*rotations

prev_p = 0

for t in range(0,steps+1):
    
    rcol = rcol + d_rcol*rcol_change
    if rcol>=255 or rcol<=0:
        d_rcol = -d_rcol
        rcol = rcol + d_rcol*rcol_change
        
    gcol = gcol + d_gcol*gcol_change
    if gcol>=255 or gcol<=0:
        d_gcol = -d_gcol
        gcol = gcol + d_gcol*gcol_change   

    bcol = bcol + d_bcol*bcol_change
    if bcol>=255 or bcol<=0:
        d_bcol = -d_bcol
        bcol = bcol + d_bcol*bcol_change        
   
    col2 = '#{:02x}{:02x}{:02x}'.format( rcol, gcol , bcol )
    # convert rgb to hex colour
    line_col(col2)
    
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    xp = xc + x
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    yp = yc + y
    line(prevx,prevy,xp,yp)  # draw the line
    prevx=xp
    prevy=yp
    angle+=theta
    p = int(angle/(2*pi))
    if p!=prev_p:
        # p = record progress - how many times inner circle
        # goes around outer circle
        print(p)  # delete this line if desired
        prev_p=p
    



finish()
display()

