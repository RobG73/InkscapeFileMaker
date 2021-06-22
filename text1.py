# Text


from ifm import *
filename = "text1.svg"
start(filename)

# Set line_width to zero, so that text doesn't have a border
line_width(0)
page_size(700,400)

line_col('#0000FF')
fill_col('#000000')

# Print text with various fonts, weights and styles

text_print("Hello World",100,50)

font("Arial",16)
text_print("Arial size 16pt",100,100)

font("Arial",16,"bold","italic")
text_print("Arial 16pt bold italic",100,150)

fill_col("#FF0000")
font_desc("TBI",16)
text_print("Times 16pt bold italic",100,200)

# font_desc("FWS",size)
#    "T" or "t": "Times New Roman"
#    "A" or "a": "Arial"
#    "S" or "s": "sans-serif"
    
#    "B" or "b": weight="bold"
#    "N" : weight="normal"

#    "I" or"i": "italic"
#    "n": style="normal"

fill_col("black")

# Left (normal) print, middle_print and right_print

font_desc("TNn",16)
text_print("text print",100,250)    
   
middle_print("middle print",100,300)

right_print("right print",100,350)


# Print text at angles

font_desc("ANn",12)
i = 0
while i < 360:
    text = "text" + str(i)
    text_print_angle(text,500,120,i,480,120)
    i += 60


fill_col("red")
font_desc("ANn",12)
i = 0
while i < 360:
    text = "text" + str(i)
    text_print_angle_rel(text,500,280,i,-30,0)
    i+=60



line_width(1)
line(100,50,100,350)
circle(480,120,1)
circle(470,280,1)

line_width(4)
line_col("red")
fill_col("yellow")
font_desc("ABn",70)
text_print("A",600,200)
fill_col("cyan")
line_col("blue")
text_print_angle("A",600,200,180,633.5,202)

finish()
display()







