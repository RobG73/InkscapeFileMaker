# Inkscape File Maker (ifm.py)

### _The easy way to create an Inkscape file from a Python program._


&nbsp;

### Introduction:

Inkscape is a free program to create illustrations as vector graphics. It has a comprehensive selection of tools to enable you to draw almost anything you can imagine.

Sometimes, however, we want to create Inkscape files from programs e.g. 

- to put items with exact measurements in the document;
- to vary the contents of the file depending e.g. on the current date;
- to draw patterns depending on equations and calculations.

Inkscape File Maker enables you to do these things, and more, from Python programs. 

The library used to create Inkscape files such as these is called **ifm.py** - it is currently at Version 0.5



&nbsp;

### Instructions:

1. Install **Inkscape** from https://inkscape.org/

1. Install **Python**:
    - If you don't have Python on your computer, then install Python 3
    - For a simple tutorial, follow this video:
      https://www.youtube.com/watch?v=96OByGW3jpI

    - For a more advanced tutorial (using virtual environments) follow this video:
    https://www.youtube.com/watch?v=28eLP22SMTA

1. **ifm** creates **.svg** files. You need to associate this filetype with Inkscape, so that the files you create will open automatically in Inkscape.
     - Search on your computer for **"Change the filetype associated with file extension"**
     - Change .svg extension to be opened by Inkscape.
     - See: https://www.thewindowsclub.com/change-file-associations-windows for help.

1. Download the zip file (including **ifm.py**) from **Github**, and unzip the contents.
     - the folder includes some test programs (see below)
     - The easiest way to use **ifm** is to put your programs in the same folder as **ifm.py**.


&nbsp;


### Example Program:

Find **rect1.py** which is a program to create a simple rectangle in an Inkscape file.

Right-click on the file, Choose **"Edit with IDLE"** -> **"Edit with IDLE 3.9 (64-bit)"**

This will open the file in IDLE, where you can change commands and experiment with the program.

Here are the commands in the program, and a detailed explanation for each of the lines:

```python
from ifm import *       <- import the ifm library
filename = "rect1.svg"  <- choose the name of the file to create
start(filename)         <- then start making it
line_width(2)           <- Choose a line-width of 2 pixels
page_size(400, 300)     <- Choose the page size - here 400 px width and 300px height
line_col('#0000FF')     <- Choose a line colour, here we choose Blue
fill_col('#00FFFF')     <- Choose a fill colour, here we choose cyan
x = 50                  <- Choose the x position of the top left corner
y = 40                  <- Choose the y position of the top left corner
width = 150             <- Choose the width of the rectangle
height = 100            <- Choose the height of the rectangle
rect(x,y,width,height)  <- Draw the rectangle
# rect(50,40,150,100)   <- or you can put it in a short command like this
finish()                <- finish the file
display()               <- automatically open and display the file (windows only)
```

To run the file from IDLE, select **"Run"** from the IDLE menu, then **"Run module"** (or press F5).
This will open the Python shell and then run the program.

If you make any changes, save the file first, by selecting **"File"**, then **"Save"** (or Save as, if you want to create a new program)

Note, the first time you run the program, it will take some time. It has to open Inkscape first, then run the python program, then load the svg file into Inkscape. (or maybe I just have a slow computer!)

There is no need to include all the explanations - though it is advisable to explain any unusual commands. Trying to edit a program with no explanations at some time in the future is not recommended!

The above program could be shortened to:

```python
from ifm import *  
start("rect1.svg") 
line_width(2)    
page_size(400, 300) 
line_col('blue')    
fill_col('cyan') 
rect(50,40,150,100)  
finish()         
display()  
```

See paragraph 2.1 below re. naming colours instead of using a hex number.


## Note:

If you click on the rectangle in Inkscape, you can see its dimensions in the four boxes at the top of the screen. The 2px line outlining the rectangle is drawn with half its thickness **inside** the rectangle, and half **outside**. This explains why the x-value is shown to be 49, rather than 50, and the y-value is 39 rather than 40. It explains too why the width is shown as 152, and the height 102 pixels. 

This can be seen more clearly in the program **rect1b.py**, where the blue border of the rectangle is made wider (8px) and slightly transparent. The fill colour is green. The part of the border outside the rectangle is blue (as expected). The part of the border inside the rectangle is overlapping the fill colour, and appears to be a darker blue-grey. If you want the rectangle to be within the dimensions you give it, you have to take account of the border width. (i.e. the value set by line_width)

&nbsp;

## List of Commands:
#### Details of the individual commands and how they are used in programs follow below.


### General commands:
- start(filename)
- finish()
- display()
- units("cm")
- line_width(line_width)
- page_size(width, height)
- page("A4")   -> Portrait
- page("A4",1) -> Landscape
- start_group()
- end_group()


### Colour commands
- fill_col(col, fill_opacity=1)
- line_col(col, line_opacity=1)
- linear_gradient(col1,col2,choice=0,opacity1=1,opacity2=1)


### Lines and shapes
- rect(xpos,ypos,width,height,rx=0,ry=0)
- circle(xpos,ypos,radius)
- ellipse(xpos,ypos,radius_x,radius_y)
- line(xpos1,ypos1,xpos2,ypos2)
- arc(xc,yc,rx,ry,theta1,theta2)
- sector(xc,yc,rx,ry,theta1,theta2)


### Path commands
- path_relative()
- path_absolute()
- start_path(xpos1,ypos1)     
- draw(xpos2,ypos2)
- move(xpos2,ypos2)
- path_arc(rx,ry,type,xpos2,ypos2)
- curve1(xposc,yposc,xpos2,ypos2)
- curve2(xposc1,yposc1,xposc2,yposc2,xpos2,ypos2)
- end_closed_path()
- end_path()


### Text commands
- font(family,size)
- text_print(text,xpos,ypos)
- text_print_angle_rel(text,xpos,ypos,degrees,xposr,yposr)
- text_print_angle(text,xpos,ypos,degrees,xposr,yposr)
- middle_print(text,xpos,ypos)
- right_print(text,xpos,ypos)

### Image commands
- print_image(src,xpos,ypos,width,height)
 

### Examples of how ifm.py could be used
- Calendar
- Table
- Spirograph - basic program
- Spirograph - add colours
- Spirograph - add colours and white
- Spirograph - completely random 
- Koch Snowflake

 
&nbsp;

&nbsp;


## Details of Commands:


&nbsp;


### 1.1) Change the units of measurement

The default unit is pixels. But you can change to "cm", "mm" or "in" (for inches) using the units command: e.g.
```python 
units("mm")
```

Put this command just after the start(filename) command. Every successive command will now use the new units. e.g. line_width(2) will create lines with width 2mm.
```python
page_size(400, 300)
```

will create a page with width 400mm and height 300mm - so you may want to change these!

See the program **rect2.py** 

&nbsp;


### 1.2) Choose page size by name:

Instead of choosing a page size by width and height (with page_size()) , you can select various paper sizes by name. e.g.
```python
page("A4")
```
This could be useful if you want to print the page onto paper of a certain size.
You can use "A4", "A5", "A6", "A7", "A8", "Letter" or "Legal".

Note that the page you create will be in Portrait format. If you want Landscape format, just add a 1 to the command:
 e.g. 
```python
page("A4", 1)
```

See the program **rect2.py**
 
&nbsp;
 
 
### 2.1) Change opacity of colours:

Using fill_col("#FF0000") and line_col("#00FF00") will choose Red fill colour and green line colour with Opacity 1, i.e. full colour, with no transparency. But you can change the opacity like this:

```python
fill_col("#FF0000")       -> full opacity
fill_col("#FF0000", 0.5)  -> Half opacity, partly transparent
fill_col("#FF0000", 0.1)  -> Almost completely transparent
fill_col("#FF0000", 0)    -> Completely transparent i.e. no fill colour
fill_col("none")          -> also gives no fill colour.
```

Add opacity to Line colour in exactly the same way.

Note: You can use names for colours instead of hexadecimal. 
e.g. 
```python
fill_col("red", 0.5)
```

Use any of the 140 colour names that can be used by css. See https://www.w3schools.com/colors/colors_names.asp

See the program **rect2.py**

&nbsp;

### 2.2) Select a gradient as a fill colour:

As an example, try the command:
```python
linear_gradient("blue","cyan",2)
```

This will create a vertical linear gradient from blue at the top to cyan at the bottom.
Use instead of the fill_col() command.

The 2 can be changed to select a different angle for the gradient:
- 0 = horizontal left to right, 
- 1 = diagonal, top left to bottom right
- 2 = vertical, top to bottom, 
- 3 = diagonal, top right to bottom left.

You can also change the opacity of the colours:
```python
linear_gradient("blue","cyan",0,0.9,0.2)
```
will select a horizontal left to right gradient (0), from blue with opacity 0.9 to cyan with opacity 0.2. 

See the program **rect2.py**

&nbsp;

### 3.1) Shapes - Rectangle:

You have already met the command to draw a rectangle:
```python
rect(x,y,width,height)
```
But you can also have a rectangle with curved corners:
```python
rect(x,y,width,height,rx,ry)
```

rx and ry are the radii of the corners in the x and y directions. Normally you should use the same value for both rx and ry. e.g. try:
```python
rect(50,40,150,100,10,10)
```
Try changing the values for rx and ry. If you give either rx or ry a value of 0, e.g. rx=0, ry=10, that will effectively be the same as giving both a value of 10. Except that when you double-click on the rectangle in Inkscape, you will see only one control point on each corner. Giving rx and ry different (non-zero) values, gives the rectangle a strange shape with two different radii at the corners. e.g.
```python
rect(50,40,150,100,20,5)
```
You may find some use to these lozenge-type shapes.

See examples of a rectangle in the program **rect2.py** 
The program also includes the commands in paragraphs 1 to 5 above.
In Inkscape, change the units from px to mm, and click on the rectangle to confirm the dimensions.

&nbsp;


### 3.2) Shapes: Circle

A circle can be drawn using the command:
```python
circle(x,y,r)
```
x and y are the coordinates of the centre of the circle, and r is the radius.
e.g. Try this command:
```python
circle(150,100,50)
```
A circle can be seen in the program **circle1.py**


&nbsp;

### 3.3) Shapes: Ellipses

An ellipse can be drawn with the command:
```python
ellipse(x,y,rx,ry)
```
x and y are the coordinates of the centre of the ellipse, rx is the horizontal radius (half the width of the ellipse) and ry is the vertical radius (half of the height of the ellipse).
 
e.g. Try this command:
```python
ellipse(150,100,80,40)
```
An ellipse can be seen in the program **circle1.py**

&nbsp;


### 3.4) Shapes: Lines

A line can be drawn between two points using the command:
```python
line(x1,y1,x2,y2)
```
The line goes from the point with coordinates (x1,y1) to the point (x2,y2)

e.g. Try this command:
```python
line(0,0,150,100)
```
The line() command is used in the program **grid1.py** to draw a grid of 1 cm squares on an A4 sheet.

&nbsp;


### 3.5) Shapes: Lines with arrows

A line with arrows can be drawn between two points using the command:
```python
line(x1,y1,x2,y2,a1,a2)
```
The line goes from the point with coordinates (x1,y1) to the point (x2,y2).
If a1 is larger than zero, then an arrow will be drawn at (x1,y1) with width equal to a1 times the current line width.
If a2 is larger than zero, then an arrow will be drawn at (x2,y2) with width equal to a2 times the current line width.

Both the line colour and fill colour must be assigned for the arrows to be visible.
The colour of the arrow depends only on the fill colour, and can be different to the line colour.

See the program **lines1.py** for examples.



&nbsp;


### 3.6) Shapes: Arcs

An arc can be drawn using the command:
```python
arc(xc,yc,rx,ry,theta1,theta2)
```
The arc is simply part of an ellipse. 

**xc** and **yc** are the coordinates of the centre of the ellipse, **rx** is the horizontal radius (half the width of the ellipse) and **ry** is the vertical radius (half of the height of the ellipse). The arc subtends the angle between **theta1** degrees and **theta2** degrees, and is drawn **clockwise**.

Because the arc is always drawn clockwise from theta1 to theta2, the command:

```python
arc(xc,yc,rx,ry,30,330)
```
will draw a **long** clockwise arc, which passes through 90&deg;, 180&deg; and 270&deg;, before reaching 330&deg;. On the other hand, the command:

```python
arc(xc,yc,rx,ry,330,30)
```
draws a **short** clockwise arc, which passes through 0&deg;.

If **rx** and **ry** are equal, then the arc is part of a circle. See the program **arcs2.py** for examples of arcs of both ellipses and circles.

**Note** that angles in Inkscape start at the normal zero, but increase **clockwise**, (not anticlockwise, as in normal geometry)


&nbsp;

### 3.7) Shapes: Sectors

A sector can be drawn using the command:
```python
sector(xc,yc,rx,ry,theta1,theta2)
```

Note that this is similar to the command for **arc**, with all the same variables.
**xc** and **yc** are the coordinates of the centre of the ellipse, **rx** is the horizontal radius (half the width of the ellipse) and **ry** is the vertical radius (half of the height of the ellipse). The sector subtends the angle between **theta1** degrees and **theta2** degrees, and is drawn **clockwise**.

A sector is simply an arc, together with lines joining the ends of the arc to the centre of the ellipse. It is a closed path, and so can be filled with the command **fill_col()**.

See the program **arcs2.py** for examples.

&nbsp;


### 4) Paths

A path consists of multiple parts such as lines, moves or various types of curves.
After describing all the commands available to draw paths, programs will be listed to illustrate their use.

&nbsp;


### 4.1) Paths: Start path

A path always starts with the command
```python
start_path(x1,y1)
```
The path will start from this position (x1,y1)
Imagine that Path commands move an imaginary "pen".


&nbsp;


### 4.2) Paths: draw lines

A straight line can be drawn from the start of the path to a new point using the command:
```python
draw(x2,y2)
```
The pen will draw a line from (x1,y1) to (x2,y2)
    

&nbsp;


### 4.3) Paths: move (by drawing an invisible line)

The "pen" can move to a new position using the command:
```python
move(x3,y3)
```
This is still part of the path, but there is no line to be seen.

&nbsp;


### 4.4) Paths: Arcs

An arc can be drawn from the previous position of the "pen" to a new point, using the command:
```python
path_arc(rx,ry,type,x2,y2)
```
If rx and ry are equal, then this will draw an arc of a circle (of radius rx or ry) from the previous position of the pen to the point (x2,y2). 

If rx and ry are not equal, then this will draw an arc of an ellipse (of x-radius rx and y-radius ry) from the previous position of the pen to the point (x2,y2). 

Four different arcs with the same radii can be drawn between two points.
- If type=1 then the clockwise short arc will be drawn. 
- If type=2 you will get anticlockwise short arc. 
- If type=3 the clockwise long arc will be drawn, and finally ... 
- if type=4 the anticlockwise long arc will be drawn.

See the program **path_arcs.py** for examples.


&nbsp;


### 4.5) Paths: Quadratic Bezier Curve

The command:
```python
curve1(xc,yc,x2,y2)
```
will draw a quadratic bezier curve from the previous position of the "pen" to the new point (x2,y2). It will use ONE control point (xc,yc)
You can think of the control point as "pulling" the curve towards it - the further away it is, the more it distorts the curve.

See the program **curve1.py** for examples.


&nbsp;


### 4.6) Paths: Cubic Bezier Curve

The command:
```python
curve2(xc1,yc1,xc2,yc2,x2,y2):
```
will draw a cubic bezier curve from the previous position of the "pen" to the new point (x2,y2). It will use TWO control points (xc1,yc1)and (xc2,yc2).

The line from the start point to the first control point is a tangent to the start of the curve, and the line from the end point to the second control point is a tangent to the end of the curve.

See the program **curve2.py** for examples.



&nbsp;


### 4.7) Absolute and relative path coordinates

Normally, all the coordinates used in the path commands are the absolute or real coordinates of the points. But if you use the command:
```python
path_relative()
```
AFTER starting the path, then all subsequent points will be measured **RELATIVE** to the previous point. 

As an example, imagine you have:
```python
start_path(150,100)
draw(200,120)
end_path()
```
These commands will draw a line from (150,100) to (200,120) - it will move 50 units right and 20 units down.

The same line can be drawn using relative coordinates using these commands:
```python
start_path(150,100)
path_relative()
draw(50,20)
end_path()
```
The draw command now draws to a new point RELATIVE to the previous point i.e. 50 Units across and 20 units down. (Remember that positive y is down, negative y is up).

If you want to go back to absolute coordinates later in your program then use the command: 
```python
path_absolute()
```
If you don't use **path_relative()** in your program, then there is no need to issue the command **path_absolute()**. It is the default condition, and isn't needed unless to reverse the effect of **path_relative()**.

See program **path2.py** to see examples.



&nbsp;


### 4.8) Paths: End path

You must somehow end any path that has been started. There are two ways.
The first uses the command:
```python
end_path()
```
simply stops the path at the previous position of the "pen".


&nbsp;


### 4.9) Paths: End closed path

The command:
```python
end_closed_path()
```
will end the path by drawing a straight line from the previous position of the pen to the point where the path started - it CLOSES the path.

See **path1.py** for the difference between open and closed paths. In both cases the paths consist of **draw()** and **move()** commands.


&nbsp;


### 5.1) Text - default font

The default font is Times New Roman, text size is 12pt, text style and text weight both normal. So text with these characteristics can be printed using:
```python
text_print(text,xpos,ypos)
```
Try 
```python
text_print("Hello World", 100, 100)
```
Be aware that text in Inkscape is simply a path with the **outline** drawn using **line_width** and **line_colour**, and the **inner body** of the text using **fill_colour**.

To see normal text, say in black, set the **line_width(0)** and **fill_colour('black')**.



&nbsp;


### 5.2) Text - Change fonts

The font used for text, and the size of the font can be changed in two ways.
The first uses the command:
```python
font("Arial",16)
```
In place of Arial, choose the name of any font that is on your computer. The second parameter is the size of the font in points.

The above font command is equivalent to this command:
```python
font("Arial",16,"normal","normal")
```
The first "normal" refers to the weight of the font. This can be changed to "bold".
The second "normal" refers to the style of the font. This can be changed to "italic".

So to apply bold and italic to this font, use this command:
```python
font("Arial",16,"bold","italic")
```

The second way to change the font is to use the font description command:
```python
font_desc(desc,16)
```
desc is a string, like "TBI". The letters determine the character of the font.

- If there is a "T" or "t" in desc, the font will be "Times New Roman".
- If there is a "A" or "a" in desc, the font will be  "Arial"
- If there is a "S" or "s" in desc, the font will be  "sans-serif"
    
- If there is a "B" or "b" in desc, the font weight will be "bold"
- If there is a "N" in desc, the font weight will be "normal"

- If there is a "I" or"i" in desc, the font style will be "italic"
- If there is a "n" in desc, the font style will be "normal"


&nbsp;

- So font_desc("TNI",16) will be Times New Roman, normal weight, italic, 16pt.
- font_desc("SBn",14) will be sans-serif, bold weight, normal style, 14pt.
- font_desc("ANn",13) will be Arial, normal weight, normal style, 13pt.

&nbsp;
- Note the difference between "N" (normal weight) and "n" (normal style).

See the program **text1.py** for examples


&nbsp;


### 5.3) Text: Left print, right print and middle print

The command 
```python
text_print("Hello World", 100, 100) 
```
prints the string "Hello World" with the bottom **left** corner of the text at the position (100,100). So this is the equivalent to left print.

The command 
```python
middle_print("Hello World", 100, 100)
```
 prints the string "Hello World" with the bottom **centre** of the text at the position (100,100).

The command 
```python
right_print("Hello World", 100, 100)
```
prints the string "Hello World" with the bottom **right** corner of the text at the position (100,100).

See the program **text1.py** for examples.


&nbsp;


### 5.4) Text: Print at an angle
```python
text_print_angle(text,x,y,d)
```
prints the text at (x,y) but rotated by d degrees clockwise around the left bottom corner of the text. if d is negative, rotation will be anticlockwise.
```python
text_print_angle(text,x,y,d,xr,yr)
```
prints the text at (x,y), but rotated by d degrees clockwise around the absolute position (xr,yr).
```python
text_print_angle_rel(text,x,y,d,xr,yr)
```
prints the text at (x,y), but rotated by d degrees clockwise around the relative position (xr,yr). (i.e. relative to the position (x,y))

See the program **text1.py** for examples


&nbsp;


### 5.5) Text: Colour

As noted above, text is drawn with an outline set by line_width() and line_col(), and a fill colour set by fill_col(). Normally it's best to set line width to zero, and just set the text colour using fill_col(). e.g. compare black text and red text:
```python
line_width(0)
fill_col('black')
font("Arial",16)
text_print("Hello!",100,50)
# Hello! will be black
```

```python  
line_width(0)
fill_col('red')
font("Arial",16)
text_print("Hello!",100,50)
# Hello! will be red
```

But it is also possible to print text with different colour border and text fill. Usually you choose a larger font size for this. e.g. see the program **text1.py** for this example:
```python
line_width(4)
line_col("red")
fill_col("yellow")
font_desc("ABn",70)
text_print("A",600,200)
```

This is a large "A" in Arial bold 70 pt, with a red border and yellow body.


&nbsp;


### 6.1) Plot an image

In the program **print_image.py** there is this command:
```python
print_image("dog.png",50,50,123,169)
```
This prints the image "dog.png" with its top left corner at (50,50) with width 123 and height 169. You can also use "dog.jpg" instead of the png image.

You have full control of the width and height of the image.


&nbsp;


### 7.1) Use groups

Items in an Inkscape file can be placed in groups. Clicking on any item in a group selects the **whole** group; e.g. to move all the items together to a different location.

In the program **group1.py** we use these commands:
```python
start_group()
-> draw some text 
end_group()

start_group()
-> draw lines and shapes
end_group()

start_group()
-> draw two large letters
end_group()
```
There are **three** different groups produced by the program. (Note that it won't be obvious that there are groups until you click on one of the items.)

All the items between a **start_group()** and an **end_group()** command will be grouped together. 


&nbsp;

## 8) Extra programs to illustrate use of ifm.py:

### 8.1) Calendar

**calendar.py** is example of the use of the program to print an eight-week calendar. The start date can be different each time - so it is an ideal candidate for a programmable image. Look for the command:
```python
date = datetime(2021,3,29)
```
Change the date in this line - the date should always be a Monday.

**Important:** Note that you have to install **array** and **datetime** modules before running the program. To do this, you have to go to **command prompt**, i.e. while mouse pointer is in folder display, press shift and right click mouse. Select "Open command window here". Type in these commands: 
```
pip install array
pip install datetime
```


&nbsp;


### 8.2) Table

**table.py** is a program to draw a table. You can change the numbers of rows and columns, and the data that is drawn in the table.

Note that you have to install **numpy** before running this program. Go to the command prompt, i.e. in the folder, press shift and right click mouse; select "Open command window here". Type in command: 
```
pip install numpy
```

&nbsp;


### 8.3) Spirograph - basic program

**spiro1.py** is a program to draw a **Spirograph** pattern.

Experiment with different values of R, r and d - change the values as shown below. 
The pattern is drawn as one path.

```python
R = 205   # large circle radius
r = 75    # inner circle radius
d = 55    # distance from centre of inner circle
```

&nbsp;


### 8.4) Spirograph - add colours

**spiro2.py** is a program to draw a **Spirograph** pattern as with **spiro1.py**, but with varying colours.
You can change the original values of Red, Green and Blue, as well as the rate at which each of the colours changes with each iteration of the parameter **t**. Experiment with different colours.

Note that, whereas **spiro1.py** used a path to draw the pattern, **spiro2.py** uses individual **lines**, each of which can be a different colour.


&nbsp;


### 8.5) Spirograph - add colours and white

**spiro3.py** is a program to draw a **Spirograph** pattern with varying colours (as with **spiro2.py**), but after a certain fraction of the iterations of t, the lines are all drawn in white. This adds interest to the pattern, by making it more variable.

&nbsp;


### 8.6) Spirograph - completely random

**spiro4.py** is a program to draw a **Spirograph** pattern - but all the parameters and colours are completely random. So the resulting spirograph pattern is completely different each time the program is run.

The values chosen by the program are printed with the pattern in the Inkscape file. If you like the pattern and would like to store it, take a note of the values, and put them into **spiro3.py** to produce the same pattern again.

Alternatively, you could of course, save the Inkscape file under a different name. Otherwise the file will be overwritten when **spiro4.py** is run again. (See files called BestSpiro4x.svg for examples of randomly produced patterns.)


&nbsp;


### 8.7) Spirograph - turtle program

I've added another program to the folder - it's called **turtle_spiro.py**, and is a program to draw a **Spirograph** pattern **in real time**. It doesn't use **ifm.py**, but uses turtle graphics. It's based on the same mathematics as the spirograph programs above - but it's really interesting seeing the pattern being drawn **live!** 

&nbsp;

### 8.8) Koch Snowflake 

**Koch Snowflake.py** is a program to draw a **fractal** pattern, called a Koch snowflake. For details, see here: https://towardsdatascience.com/creating-fractals-with-python-d2b663786da6

&nbsp;

&nbsp;