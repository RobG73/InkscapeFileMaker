# Groups


from ifm import *
filename = "group1.svg"
start(filename)

line_width(0)
page_size(700,400)

line_col('blue')
fill_col('black')



start_group()
# group of text items
text_print("Hello World",50,50)
font("Segoe Script",16)
text_print("Segoe Script, size 16pt",50,100)
font("Arial",16,"bold","italic")
text_print("Arial 16pt bold italic",50,150)
end_group()


start_group()
# group of lines and shapes
line_width(3)
line(350,50,350,350)
line_width(2)
fill_col("yellow")
circle(480,120,50)
fill_col("coral")
circle(470,280,60)
end_group()


start_group()
# group of two large letters
line_width(4)
line_col("red")
fill_col("yellow")
font_desc("ABn",70)
text_print("A",600,200)
fill_col("cyan")
line_col("blue")
text_print_angle("A",600,200,180,633.5,202)
end_group()



finish()
display()







