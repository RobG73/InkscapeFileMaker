
# Draw a spirograph pattern
# www.101computing.net/python-turtle-spirograph/

# Added colour changes;
# Used line() commands instead of path commands
# because the whole of a path can only be one colour
# each of the "lines" can be different colours.

# Added drawing lines in white after fraction of number of steps
# adds interest to pattern.

# All parameters are randomly chosen
# - pattern different each time program is run


from ifm import *
from math import cos,sin,pi
import random

def get_rots(nR,nr):
    # Calculate number of rotations of
    # inner circle around large circle
    n=1
    while n*nR/nr!=int(n*nR/nr):
        n+=1
    return n


filename = "spiro4.svg"
start(filename)

line_col('black')
fill_col('black')
line_width(0)

rotations = 0
while rotations<=50:

    R = random.randint(150, 250)   # large circle radius
    r = random.randint(37, 97)    # inner circle radius
    d = random.randint(int(0.5*r), r)    # distance from centre of inner circle

    rotations = get_rots(R,r)


p_width = int(R*2.5)
p_height = int(R*2.5)
page_size(p_width,p_height)

font_desc("TNn",12)
text_print("R = "+str(R),20,30)
text_print("r = "+str(r),20,50)
text_print("d = "+str(d),20,70)


# rotations = get_rots(R,r)
# print(rotations)

# Original values of red,green and blue
rcol = random.randint(0, 255)
gcol = random.randint(0, 255)
bcol = random.randint(0, 255)

# Directions in which colours change
# +1 = increase amount of that colour
# -1 = decrease amount of that colour
d_rcol = 1 - 2*random.randint(0, 1)
d_gcol = 1 - 2*random.randint(0, 1)
d_bcol = 1 - 2*random.randint(0, 1)


# How much each of red, green and blue changes
# for each iteration of t
rcol_change = random.randint(1,9)
gcol_change = random.randint(1,9)
bcol_change = random.randint(1,9)

# Lower limit of red,green and blue
# The higher the value for a colour, the more that colour
# predominates in
rcol_min = random.randint(0, 128)
gcol_min = random.randint(0, 128)
bcol_min = random.randint(0, 128)



# when to draw in white
frac = (random.randint(5,9))/10

rdir = " (+" if d_rcol == 1 else " (-"
gdir = " (+" if d_gcol == 1 else " (-"
bdir = " (+" if d_bcol == 1 else " (-"

rtext = "Red = "+str(rcol)+rdir+str(rcol_change)+")"
gtext = "Green = "+str(gcol)+gdir+str(gcol_change)+")"
btext = "Blue = "+str(bcol)+bdir+str(bcol_change)+")"

right_print(rtext,p_width-20,30)
right_print(gtext,p_width-20,50)
right_print(btext,p_width-20,70)
right_print('frac = '+str(frac),p_width-20,90)

text_print("rcol_min = "+str(rcol_min),20,p_height-70)
text_print("gcol_min = "+str(gcol_min),20,p_height-50)
text_print("bcol_min = "+str(bcol_min),20,p_height-30)


# centre of large circle
xc = 0.5*p_width
yc = 0.5*p_height

angle = 0

# previous values of x and y
prevx = xc+R-r+d
prevy = yc

theta = pi/30
steps = 60*rotations
print("steps = ",steps)
if steps<2000:
    font_desc("TNn",12)
    middle_print("Predicted poor image - please run again!",p_width,0.5*p_height)
    print("Predicted poor image - please run again!")

line_col('black')
fill_col('none')
line_width(2)


prev_p = 0

for t in range(0,steps+1):
    
    rcol = rcol + d_rcol*rcol_change
    if rcol>=255 or rcol<=rcol_min:
        d_rcol = -d_rcol
        rcol = rcol + d_rcol*rcol_change
        
    gcol = gcol + d_gcol*gcol_change
    if gcol>=255 or gcol<=gcol_min:
        d_gcol = -d_gcol
        gcol = gcol + d_gcol*gcol_change   

    bcol = bcol + d_bcol*bcol_change
    if bcol>=255 or bcol<=bcol_min:
        d_bcol = -d_bcol
        bcol = bcol + d_bcol*bcol_change

    # draw lines in white after fraction of steps
    if t>frac*steps:
        rcol=255
        gcol=255
        bcol=255
   
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
        # print(p)  # undelete this line if desired
        prev_p=p
    

print("Rotations = ",prev_p)

finish()
display()

