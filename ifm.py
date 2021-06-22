# Inkscape File Maker (IFM)
# Use this library to create inkscape files
# from simple python commands

# 0.2 added style and weight to fonts
# 0.3 added arrows to lines
# 0.3 added groups
# 0.4 changed start_path and end_closed_path
#     because end_closed_path closes path to end of last move statement
#     - new version draws line to beginning of path
# 0.5 arc changed to path_arc, to emphasise that it must be part of path,
#     and to create new stand-alone function arc(xc,yc,rx,ry,theta1,theta2)
#     and similar function sector(xc,yc,rx,ry,theta1,theta2)

import numpy

# defining the atan function
# https://stackoverflow.com/questions/35749246/python-atan-or-atan2-what-should-i-use
myatan = lambda x,y: numpy.pi*(1.0-0.5*(1+numpy.sign(x))*(1-numpy.sign(y**2))\
         -0.25*(2+numpy.sign(x))*numpy.sign(y))\
         -numpy.sign(x*y)*numpy.arctan((numpy.abs(x)-numpy.abs(y))/(numpy.abs(x)+numpy.abs(y)))




def fill_col(svg_col, svg_fill_opacity=1):
    global global_fill_col
    global global_fill_opacity
    if svg_fill_opacity==1:
        global_fill_col = svg_col
        global_fill_opacity = 1
    if svg_fill_opacity<1:
        global_fill_col = svg_col
        global_fill_opacity = svg_fill_opacity;
    if svg_col=='none':
        global_fill_col = 'none'
        global_fill_opacity = 0


def line_col(svg_col, svg_line_opacity=1):
    global global_line_col
    global global_line_opacity
    if svg_line_opacity==1:
        global_line_col = svg_col
        global_line_opacity = svg_line_opacity
    if svg_line_opacity<1:
        global_line_col = svg_col
        global_line_opacity = svg_line_opacity    
    

def line_width(svg_line_width):
    global global_line_width
    global_line_width = global_units_multiplier * svg_line_width
    global_line_width = round(global_line_width,3)
    


def units(svg_units):
    global global_units_multiplier
    global_units_multiplier = 1
    if svg_units=="cm":
        global_units_multiplier = 37.7952
    if svg_units=="mm":
        global_units_multiplier = 3.77952
    if svg_units=="in" or svg_units=="inches":
        global_units_multiplier = 96
    

def page_size(n_svg_width, n_svg_height):
    svg_width = round(global_units_multiplier * n_svg_width, 3)
    svg_height = round(global_units_multiplier * n_svg_height, 3)
    svg_line = '<?xml version="1.0" standalone="no"?>\n'
    svg_line += '<svg\n'
    svg_line += 'width="' + str(svg_width) + 'px"\n'
    svg_line += 'height="' + str(svg_height) + 'px"\n'
    svg_line += 'viewBox="0 0 ' + str(svg_width) + ' ' + str(svg_height) + '">\n'
    svg_line += ' <sodipodi:namedview\n'
    svg_line += '    inkscape:window-maximized="1"\n'
    svg_line += '    showguides="true">\n'
    svg_line += ' </sodipodi:namedview>\n'
    global_svg_file_handle.write(svg_line)
    


def page(n_desc, n_landscape=0):
    global global_units_multiplier
    store_global_units_multiplier = global_units_multiplier
    if n_desc=='A4' or n_desc=='a4':
        units('cm')
        if n_landscape==0:
            page_size(21,29.7)
        else:
            page_size(29.7,21)
    elif n_desc=='A5' or n_desc=='a5':
        units('cm')
        if n_landscape==0:
            page_size(14.8,21)
        else:
            page_size(21,14.8)
    elif n_desc=='A6' or n_desc=='a6':
        units('cm')
        if n_landscape==0:
            page_size(10.5,14.8)
        else:
            page_size(14.8,10.5)
    elif n_desc=='A7' or n_desc=='a7':
        units('cm')
        if n_landscape==0:
            page_size(7.4,10.5)
        else:
            page_size(10.5,7.4)
    elif n_desc=='A8' or n_desc=='a8':
        units('cm')
        if n_landscape==0:
            page_size(5.2,7.4)
        else:
            page_size(7.4,5.2)
    elif n_desc=='Letter' or n_desc=='letter':
        units('in')
        if n_landscape==0:
            page_size(8.5,11)
        else:
            page_size(11,8.5)    
    elif n_desc=='Legal' or n_desc=='legal':
        units('in')
        if n_landscape==0:
            page_size(8.5,14)
        else:
            page_size(14,8.5)
    global_units_multiplier = store_global_units_multiplier
        
        


def rect(n_xpos,n_ypos,n_width,n_height, n_rx=0, n_ry=0):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    width = round(global_units_multiplier * n_width, 3)
    height = round(global_units_multiplier * n_height, 3)
    rx = round(global_units_multiplier * n_rx, 3)
    ry = round(global_units_multiplier * n_ry, 3)
    svg_line =  '<rect '
    svg_line += ' x="' + str(xpos) + '" '
    svg_line += ' y="' + str(ypos) + '" '
    svg_line += ' rx="' + str(rx) + '" '
    svg_line += ' ry="' + str(ry) + '" '
    svg_line += ' width="' + str(width) + '" '
    svg_line += ' height="' + str(height) + '" '
    svg_line += ' style="'
    svg_line += ' fill: ' + global_fill_col + '; '
    svg_line += ' fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += ' stroke: ' + global_line_col + '; '
    svg_line += ' stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += ' stroke-width: ' + str(global_line_width) + '; " '
    svg_line += ' />'    
    global_svg_file_handle.write(svg_line)



def circle(n_xpos,n_ypos,n_radius):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    radius = round(global_units_multiplier * n_radius, 3)
    svg_line =  '<circle '
    svg_line += ' cx="' + str(xpos) + '" '
    svg_line += ' cy="' + str(ypos) + '" '
    svg_line += ' r="' + str(radius) + '" '
    svg_line += ' style="'
    svg_line += ' fill: ' + global_fill_col + '; '
    svg_line += ' fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += ' stroke: ' + global_line_col + '; '
    svg_line += ' stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += ' stroke-width: ' + str(global_line_width) + '; " '
    svg_line += ' />'    
    global_svg_file_handle.write(svg_line)    



def ellipse(n_xpos,n_ypos,n_radius_x, n_radius_y):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    radius_x = round(global_units_multiplier * n_radius_x, 3)
    radius_y = round(global_units_multiplier * n_radius_y, 3)
    svg_line =  '<ellipse '
    svg_line += ' cx="' + str(xpos) + '" '
    svg_line += ' cy="' + str(ypos) + '" '
    svg_line += ' rx="' + str(radius_x) + '" '
    svg_line += ' ry="' + str(radius_y) + '" '
    svg_line += ' style="'
    svg_line += ' fill: ' + global_fill_col + '; '
    svg_line += ' fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += ' stroke: ' + global_line_col + '; '
    svg_line += ' stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += ' stroke-width: ' + str(global_line_width) + '; " '
    svg_line += ' />'    
    global_svg_file_handle.write(svg_line)    
    


def arc(n_xc,n_yc,n_rx,n_ry,n_theta1,n_theta2):
    # draw elliptical arc
    # centre of arc at xc,yc
    # x-radius rx and y-radius ry
    # from theta1 to theta2 (measured from centre of ellipse)
    import math

    xc = round(global_units_multiplier * n_xc, 3)
    yc = round(global_units_multiplier * n_yc, 3)
    rx = round(global_units_multiplier * n_rx, 3)
    ry = round(global_units_multiplier * n_ry, 3)
    theta1 = round(math.radians(n_theta1), 3)
    theta2 = round(math.radians(n_theta2), 3)

    dtheta = n_theta2-n_theta1
    if dtheta<0:
        dtheta=dtheta+360
    if dtheta<180:
        type=1
    else:
        type=3
    
    ax1 = rx*math.sin(theta1)
    ay1 = ry*math.cos(theta1)
    alpha1 = myatan(ay1,ax1)
    xp1 = rx*math.cos(alpha1)
    yp1 = ry*math.sin(alpha1)
    xpos1 = xc + xp1
    ypos1 = yc + yp1

    ax2 = rx*math.sin(theta2)
    ay2 = ry*math.cos(theta2)
    alpha2 = myatan(ay2,ax2)
    xp2 = rx*math.cos(alpha2)
    yp2 = ry*math.sin(alpha2)
    xpos2 = xc + xp2
    ypos2 = yc + yp2
    
    start_path(xpos1,ypos1)
    path_arc(rx,ry,type,xpos2,ypos2)
    end_path()
    #type = 1 or 3 for clockwise

    
def sector(n_xc,n_yc,n_rx,n_ry,n_theta1,n_theta2):
    # draw elliptical sector
    # centre of ellipse at xc,yc
    # x-radius rx and y-radius ry
    # from theta1 to theta2 (measured from centre of ellipse)
    import math

    xc = round(global_units_multiplier * n_xc, 3)
    yc = round(global_units_multiplier * n_yc, 3)
    rx = round(global_units_multiplier * n_rx, 3)
    ry = round(global_units_multiplier * n_ry, 3)
    theta1 = round(math.radians(n_theta1), 3)
    theta2 = round(math.radians(n_theta2), 3)

    dtheta = n_theta2-n_theta1
    if dtheta<0:
        dtheta=dtheta+360
    if dtheta<180:
        type=1
    else:
        type=3
    
    ax1 = rx*math.sin(theta1)
    ay1 = ry*math.cos(theta1)
    alpha1 = myatan(ay1,ax1)
    xp1 = rx*math.cos(alpha1)
    yp1 = ry*math.sin(alpha1)
    xpos1 = xc + xp1
    ypos1 = yc + yp1

    ax2 = rx*math.sin(theta2)
    ay2 = ry*math.cos(theta2)
    alpha2 = myatan(ay2,ax2)
    xp2 = rx*math.cos(alpha2)
    yp2 = ry*math.sin(alpha2)
    xpos2 = xc + xp2
    ypos2 = yc + yp2
    
    start_path(xpos1,ypos1)
    path_arc(rx,ry,type,xpos2,ypos2)
    draw(xc,yc)
    end_closed_path()
    #type = 1 or 3 for clockwise


def line(n_xpos1,n_ypos1,n_xpos2,n_ypos2,start_arrow=0,end_arrow=0):
    import math
    global global_line_width
    global global_arrow_angle                
    start_group()
    xpos1 = round(global_units_multiplier * n_xpos1, 3)
    ypos1 = round(global_units_multiplier * n_ypos1, 3)
    xpos2 = round(global_units_multiplier * n_xpos2, 3)
    ypos2 = round(global_units_multiplier * n_ypos2, 3)
    if end_arrow>0:
        # x1,y1 to x2,y2   arrow at x2,y2        
        theta1 = 0.5*global_arrow_angle
        theta = math.radians(theta1)
        dx = xpos1 - xpos2
        dy = ypos1 - ypos2
        Norm = math.sqrt(dx*dx + dy*dy)
        udx = dx/Norm
        udy = dy/Norm
        ax = udx*math.cos(theta) - udy*math.sin(theta)
        ay = udx*math.sin(theta) + udy*math.cos(theta)
        bx = udx*math.cos(theta) + udy*math.sin(theta)
        by = -udx*math.sin(theta) + udy*math.cos(theta)
        arl = end_arrow*global_line_width
        store_global_line_width = global_line_width
        global_line_width = 0
        x2a = xpos2 + arl * ax
        y2a = ypos2 + arl * ay
        x2b = xpos2 + arl * bx
        y2b = ypos2 + arl * by
        x2c = 0.5*(x2a + x2b)
        y2c = 0.5*(y2a + y2b)
        start_path(x2a,y2a)
        draw(xpos2,ypos2)
        draw(x2b,y2b)
        end_closed_path()
        global_line_width = store_global_line_width
    if start_arrow>0:
        # x2,y2 to x1,y1   arrow at x1,y1
        theta1 = 0.5*global_arrow_angle
        theta = math.radians(theta1)
        dx = xpos2 - xpos1
        dy = ypos2 - ypos1
        Norm = math.sqrt(dx*dx + dy*dy)
        udx = dx/Norm
        udy = dy/Norm
        ax = udx*math.cos(theta) - udy*math.sin(theta)
        ay = udx*math.sin(theta) + udy*math.cos(theta)
        bx = udx*math.cos(theta) + udy*math.sin(theta)
        by = -udx*math.sin(theta) + udy*math.cos(theta)
        arl = start_arrow*global_line_width
        store_global_line_width = global_line_width
        global_line_width = 0
        x1a = xpos1 + arl * ax
        y1a = ypos1 + arl * ay
        x1b = xpos1 + arl * bx
        y1b = ypos1 + arl * by
        x1c = 0.5*(x1a + x1b)
        y1c = 0.5*(y1a + y1b)
        start_path(x1a,y1a)
        draw(xpos1,ypos1)
        draw(x1b,y1b)
        end_closed_path()
        global_line_width = store_global_line_width
    # draw line
    if start_arrow>0:
        xpos1 = x1c
        ypos1 = y1c
    if end_arrow>0:
        xpos2 = x2c
        ypos2 = y2c
    xpos1 = round(xpos1, 3)
    ypos1 = round(ypos1, 3)
    xpos2 = round(xpos2, 3)
    ypos2 = round(ypos2, 3)
    svg_line =  '<line '
    svg_line += 'stroke="' + global_line_col + '" '
    svg_line += ' stroke-width="' + str(global_line_width) + '" '
    svg_line += ' x1="' + str(xpos1) + '" '
    svg_line += ' y1="' + str(ypos1) + '" ' 
    svg_line += ' x2="' + str(xpos2) + '" '
    svg_line += ' y2="' + str(ypos2) + '" ' 
    svg_line += ' />'    
    global_svg_file_handle.write(svg_line)
    end_group()
    
        



def start_group():
    import random
    svg_line =  '<g'
    svg_line +=  ' id="g'
    rn = random.randint(101, 999)
    ## rn = 819
    svg_line +=  str(rn)
    svg_line +=  '">'
    global_svg_file_handle.write(svg_line)


def end_group():
    svg_line =  '\n</g>\n'
    global_svg_file_handle.write(svg_line)

    


def path_relative():
    # global_path_relative = 1 for relative measurements
    global global_path_relative
    global_path_relative = 1;


def path_absolute():
    # global_path_relative = 0 for absolute measurements
    global global_path_relative
    global_path_relative = 0;
    


def start_path(n_xpos1,n_ypos1):
    # global_path_relative = 1 for relative measurements
    # global_path_relative = 0 for absolute measurements
    global global_path_relative
    global global_path_x0
    global global_path_y0
    xpos1 = round(global_units_multiplier * n_xpos1, 3)
    ypos1 = round(global_units_multiplier * n_ypos1, 3)
    global_path_x0 = xpos1
    global_path_y0 = ypos1
    svg_line = '<path d="'
    if global_path_relative==0:
        svg_line += 'M' + str(xpos1) + ','
        svg_line += str(ypos1) + ' '
    if global_path_relative==1:
        svg_line += 'm' + str(xpos1) + ','
        svg_line += str(ypos1) + ' '
    global_svg_file_handle.write(svg_line)


        
def draw(n_xpos2,n_ypos2):
    # draw a line from the previous point to this new point
    # only as part of path
    xpos2 = round(global_units_multiplier * n_xpos2, 3)
    ypos2 = round(global_units_multiplier * n_ypos2, 3)
    if global_path_relative==0:
        svg_line = 'L' + str(xpos2) + ','
        svg_line += str(ypos2) + ' '
    if global_path_relative==1:
        svg_line = 'l' + str(xpos2) + ','
        svg_line += str(ypos2) + ' '
    global_svg_file_handle.write(svg_line)


    

def move(n_xpos2,n_ypos2):
    # move from the previous point to this new point
    # without drawing a line - only as part of path
    xpos2 = round(global_units_multiplier * n_xpos2, 3)
    ypos2 = round(global_units_multiplier * n_ypos2, 3)
    if global_path_relative==0:
        svg_line = 'M' + str(xpos2) + ','
        svg_line += str(ypos2) + ' '
    if global_path_relative==1:
        svg_line = 'm' + str(xpos2) + ','
        svg_line += str(ypos2) + ' '
    global_svg_file_handle.write(svg_line)



def path_arc(n_rx,n_ry,n_type,n_xpos2,n_ypos2):
    # draw elliptical arc with x-radius rx (1st)
    # y-radius ry (2nd), to xpos2 (6th),ypos2(7th)
    # x-axis rotation is set to zero (3rd)
    # type = 1 short arc clockwise
    # type = 2 short arc anticlockwise
    # type= 3 long arc clockwise
    # type = 4 long arc anticlockwise
    # type sets values of large-arc-flag (4th)
    # and sweepflag (5th)
    # ONLY as part of path()
    rx = round(global_units_multiplier * n_rx, 3)
    ry = round(global_units_multiplier * n_ry, 3)
    xpos2 = round(global_units_multiplier * n_xpos2, 3)
    ypos2 = round(global_units_multiplier * n_ypos2, 3)
    if global_path_relative==0:        
        svg_line = 'A' + str(rx) + ','
        svg_line += str(ry) + ' 0 '
    if global_path_relative==1:        
        svg_line = 'a' + str(rx) + ','
        svg_line += str(ry) + ' 0 '
    if n_type==1:
        svg_line += ' 0,1 '
    if n_type==2:
        svg_line += ' 0,0 '
    if n_type==3:
        svg_line += ' 1,1 '
    if n_type==4:
        svg_line += ' 1,0 '
    svg_line += str(xpos2) + ','
    svg_line += str(ypos2) + ' '
    global_svg_file_handle.write(svg_line)

  

def curve1(n_xposc,n_yposc,n_xpos2,n_ypos2):
    # draw a quadratic bezier curve from the previous point
    # to this new point (xpos2,ypos2)
    # using ONE control point (xposc,yposc)
    # only as part of path;
    # control point "pulls" curve towards it
    xposc = round(global_units_multiplier * n_xposc, 3)
    yposc = round(global_units_multiplier * n_yposc, 3)
    xpos2 = round(global_units_multiplier * n_xpos2, 3)
    ypos2 = round(global_units_multiplier * n_ypos2, 3)
    if global_path_relative==0:
        svg_line = 'Q' + str(xposc) + ','
        svg_line += str(yposc) + ' '
        svg_line += str(xpos2) + ','
        svg_line += str(ypos2) + ''
    if global_path_relative==1:
        svg_line = 'q' + str(xposc) + ','
        svg_line += str(yposc) + ' '
        svg_line += str(xpos2) + ','
        svg_line += str(ypos2) + ''        
    global_svg_file_handle.write(svg_line)



def curve2(n_xposc1,n_yposc1,n_xposc2,n_yposc2,n_xpos2,n_ypos2):
    # draw a cubic bezier curve from the previous point
    # to this new point (xpos2,ypos2)
    # using TWO control points (xposc1,yposc1) and (xposc2,yposc2)
    # only as part of path;
    # The line from the start point to the first control point is
    # a tangent to the start of the curve
    # The line from the end point to the second control point
    # is a tangent to the end of the curve
    xposc1 = round(global_units_multiplier * n_xposc1, 3)
    yposc1 = round(global_units_multiplier * n_yposc1, 3)
    xposc2 = round(global_units_multiplier * n_xposc2, 3)
    yposc2 = round(global_units_multiplier * n_yposc2, 3)
    xpos2 = round(global_units_multiplier * n_xpos2, 3)
    ypos2 = round(global_units_multiplier * n_ypos2, 3)
    if global_path_relative==0:
        svg_line = 'C' + str(xposc1) + ','
        svg_line += str(yposc1) + ' '
        svg_line += str(xposc2) + ','
        svg_line += str(yposc2) + ' '        
        svg_line += str(xpos2) + ','
        svg_line += str(ypos2) + ''
    if global_path_relative==1:
        svg_line = 'c' + str(xposc) + ','
        svg_line += str(yposc1) + ' '
        svg_line += str(xposc2) + ','
        svg_line += str(yposc2) + ' '        
        svg_line += str(xpos2) + ','
        svg_line += str(ypos2) + ''   
    global_svg_file_handle.write(svg_line)
   


def old_end_closed_path():
    # end the path by drawing a line from the previous point
    # to the point at the start of the path
    if global_path_relative==0:
        svg_line = 'Z' + '"'        
    if global_path_relative==1:
        svg_line = 'z' + '"'
    svg_line += ' style="'
    svg_line += ' fill: ' + global_fill_col + '; '
    svg_line += ' fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += ' stroke: ' + global_line_col + '; '
    svg_line += ' stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += ' stroke-width: ' + str(global_line_width) + '; " '
    svg_line += ' />'        
    global_svg_file_handle.write(svg_line)


def end_closed_path():
    # end the path by drawing a line from the previous point
    # to the point at the start of the path
    global_path_relative = 0;
    draw(global_path_x0,global_path_y0)
    end_path()


def end_open_path():
    end_path()


def end_path():
    # end the path at the previous point
    svg_line = '"'        
    svg_line += ' style="'
    svg_line += ' fill: ' + global_fill_col + '; '
    svg_line += ' fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += ' stroke: ' + global_line_col + '; '
    svg_line += ' stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += ' stroke-width: ' + str(global_line_width) + '; " '
    svg_line += ' />'        
    global_svg_file_handle.write(svg_line)
    



def text_print(n_text,n_xpos,n_ypos):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    text = n_text
    svg_line =  '<text '
    svg_line += ' x="' + str(xpos) + '" '
    svg_line += ' y="' + str(ypos) + '" '
    svg_line += 'fill="' + global_fill_col + '" '
    svg_line += 'stroke="' + global_line_col + '" '
    svg_line += 'style="'
    svg_line += 'fill: ' + global_fill_col + '; '
    svg_line += 'fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += 'stroke: ' + global_line_col + '; '
    svg_line += 'stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += 'stroke-width: ' + str(global_line_width) + '; '
    svg_line += 'font-family: ' + global_font_family + '; '
    svg_line += 'font-weight: ' + global_font_weight + '; '
    svg_line += 'font-style: ' + global_font_style + '; '
    svg_line += 'font-size  : ' + str(global_font_size) + 'pt; " '
    svg_line += '>' + text + '</text>'   
    global_svg_file_handle.write(svg_line)



def text_print_angle_rel(n_text,n_xpos,n_ypos,n_degrees,n_xposr=999,n_yposr=999):
    # rotate text by n_degrees clockwise, around point xpos,ypos
    # or around relative position (xposr,yposr) if included in call.
    # if n_degrees is negative, rotation will be anticlockwise
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    if n_xposr==999:
        xposr = round(global_units_multiplier * n_xpos, 3)
    else:
        xposr = round(global_units_multiplier * (n_xposr + n_xpos), 3)
    if n_yposr==999:
        yposr = round(global_units_multiplier * n_ypos, 3)
    else:
        yposr = round(global_units_multiplier * (n_yposr + n_ypos), 3)
    degrees = round(n_degrees, 3)
    text = n_text
    svg_line =  '<text '
    svg_line += ' x="' + str(xpos) + '" '
    svg_line += ' y="' + str(ypos) + '" '
    svg_line += 'style="'
    svg_line += 'fill: ' + global_fill_col + '; '
    svg_line += 'fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += 'stroke: ' + global_line_col + '; '
    svg_line += 'stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += 'stroke-width: ' + str(global_line_width) + '; '
    svg_line += 'font-family: ' + global_font_family + '; '
    svg_line += 'font-weight: ' + global_font_weight + '; '
    svg_line += 'font-style: ' + global_font_style + '; '
    svg_line += 'font-size  : ' + str(global_font_size) + 'pt; " '
    svg_line += 'transform="'
    svg_line += 'rotate(' + str(degrees) + ', '
    svg_line += str(xposr) + ', '
    svg_line += str(yposr) + ')" '
    svg_line += '>' + text + '</text>'   
    global_svg_file_handle.write(svg_line)

    



def text_print_angle(n_text,n_xpos,n_ypos,n_degrees,n_xposr=999,n_yposr=999):
    # rotate text by n_degrees clockwise, around point xpos,ypos
    # or around absolute position (xposr,yposr) if included in call.
    # if n_degrees is negative, rotation will be anticlockwise
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    if n_xposr==999:
        xposr = round(global_units_multiplier * n_xpos, 3)
    else:
        xposr = round(global_units_multiplier * n_xposr, 3)
    if n_yposr==999:
        yposr = round(global_units_multiplier * n_ypos, 3)
    else:
        yposr = round(global_units_multiplier * n_yposr, 3)
    degrees = round(n_degrees, 3)
    text = n_text
    svg_line =  '<text '
    svg_line += ' x="' + str(xpos) + '" '
    svg_line += ' y="' + str(ypos) + '" '
    svg_line += 'style="'
    svg_line += 'fill: ' + global_fill_col + '; '
    svg_line += 'fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += 'stroke: ' + global_line_col + '; '
    svg_line += 'stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += 'stroke-width: ' + str(global_line_width) + '; '
    svg_line += 'font-family: ' + global_font_family + '; '
    svg_line += 'font-weight: ' + global_font_weight + '; '
    svg_line += 'font-style: ' + global_font_style + '; '
    svg_line += 'font-size  : ' + str(global_font_size) + 'pt; " '
    svg_line += 'transform="'
    svg_line += 'rotate(' + str(degrees) + ', '
    svg_line += str(xposr) + ', '
    svg_line += str(yposr) + ')" '
    svg_line += '>' + text + '</text>'   
    global_svg_file_handle.write(svg_line)

    


def middle_print(n_text,n_xpos,n_ypos):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    text = n_text
    svg_line =  '<text '
    svg_line += ' x="' + str(xpos) + '" '
    svg_line += ' y="' + str(ypos) + '" '
    svg_line += 'fill="' + global_fill_col + '" '
    svg_line += 'stroke="' + global_line_col + '" '
    svg_line += 'style="'
    svg_line += 'text-anchor: middle' + '; '
    svg_line += 'fill: ' + global_fill_col + '; '
    svg_line += 'fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += 'stroke: ' + global_line_col + '; '
    svg_line += 'stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += 'stroke-width: ' + str(global_line_width) + '; '
    svg_line += 'font-family: ' + global_font_family + '; '
    svg_line += 'font-weight: ' + global_font_weight + '; '
    svg_line += 'font-style: ' + global_font_style + '; '
    svg_line += 'font-size  : ' + str(global_font_size) + 'pt; " '
    svg_line += '>' + text + '</text>'   
    global_svg_file_handle.write(svg_line)



def right_print(n_text,n_xpos,n_ypos):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    text = n_text
    svg_line =  '<text '
    svg_line += ' x="' + str(xpos) + '" '
    svg_line += ' y="' + str(ypos) + '" '
    svg_line += 'fill="' + global_fill_col + '" '
    svg_line += 'stroke="' + global_line_col + '" '
    svg_line += 'style="'
    svg_line += 'text-anchor: end' + '; '
    svg_line += 'fill: ' + global_fill_col + '; '
    svg_line += 'fill-opacity: ' + str(global_fill_opacity) + '; '
    svg_line += 'stroke: ' + global_line_col + '; '
    svg_line += 'stroke-opacity: ' + str(global_line_opacity) + '; '
    svg_line += 'stroke-width: ' + str(global_line_width) + '; '
    svg_line += 'font-family: ' + global_font_family + '; '
    svg_line += 'font-weight: ' + global_font_weight + '; '
    svg_line += 'font-style: ' + global_font_style + '; '
    svg_line += 'font-size  : ' + str(global_font_size) + 'pt; " '
    svg_line += '>' + text + '</text>'   
    global_svg_file_handle.write(svg_line)

    

def font_desc(n_desc,n_size):
    global global_font_family
    global global_font_size
    global global_font_style
    global global_font_weight  
    if n_desc.find("T")>=0 or n_desc.find("t")>=0:
        global_font_family="Times New Roman"
    if n_desc.find("A")>=0 or n_desc.find("a")>=0:
        global_font_family="Arial"
    if n_desc.find("S")>=0 or n_desc.find("s")>=0:
        global_font_family="sans-serif"
    if n_desc.find("B")>=0 or n_desc.find("b")>=0:
        global_font_weight="bold"
    if n_desc.find("I")>=0 or n_desc.find("i")>=0:
        global_font_style="italic"
    if n_desc.find("N")>=0:
        global_font_weight="normal"
    if n_desc.find("n")>=0:
        global_font_style="normal"
    global_font_size = n_size



def font(n_family,n_size,n_weight="normal",n_style="normal"):
    global global_font_family
    global global_font_size
    global global_font_style
    global global_font_weight
    global_font_family = n_family
    global_font_size = n_size
    global_font_style = n_style
    global_font_weight = n_weight



def print_image(n_src,n_xpos,n_ypos,n_width,n_height):
    xpos = round(global_units_multiplier * n_xpos, 3)
    ypos = round(global_units_multiplier * n_ypos, 3)
    width = round(global_units_multiplier * n_width, 3)
    height = round(global_units_multiplier * n_height, 3)
    svg_line = '\n <image\n'
    svg_line += ' xlink:href="' + n_src + '"\n'
    svg_line += '   width="' + str(width) +'"\n'
    svg_line += '    height="' + str(height) + '"\n'
    # svg_line += '    preserveAspectRatio="none"\n'
    # svg_line += '    id="image21"\n'
    svg_line += '    x="' + str(xpos) + '"\n'
    svg_line += '    y="' + str(ypos) + '" />\n'
    global_svg_file_handle.write(svg_line)


    
def linear_gradient(col1,col2,choice=0,opacity1=1,opacity2=1):
    # gradient from col1 to col2
    # choice gives angle; 0 = 0 deg, 1 = 45 deg, 2 = 90 deg, 3 = 135 deg
    # 0 = horizontal left to right, 1 = diagonal, top left to bottom right
    # 2 = vertical, top to bottom, 3 = diagonal, top right to bottom left.
    # opacity = 1 is full colour, = 0 is fully transparent
    global global_fill_col
    svg_line = '<defs>\n'
    svg_line += ' <linearGradient id="n_linear_gradient_id"\n'
    if choice>=3:
        choice=3
    if choice<=0:
        choice=0
    if choice==0:
        svg_line += '   x1="0%" y1="0%"\n'
        svg_line += '   x2="100%" y2="0%"\n'
    if choice==1:
        svg_line += '   x1="0%" y1="0%"\n'
        svg_line += '   x2="100%" y2="100%"\n'
    if choice==2:
        svg_line += '   x1="0%" y1="0%"\n'
        svg_line += '   x2="0%" y2="100%"\n'
    if choice==3:
        svg_line += '   x1="100%" y1="0%"\n'
        svg_line += '   x2="0%" y2="100%"\n'
    # svg_line += '   gradientTransform = "rotate(' + str(theta) + ')"\n'
    svg_line += '   spreadMethod="pad">\n'
    svg_line += '   <stop offset="0%"   stop-color="' + col1 + '" stop-opacity="' + str(opacity1) + '"/>\n'
    svg_line += '   <stop offset="100%" stop-color="' + col2 + '" stop-opacity="' + str(opacity2) + '"/>\n'
    svg_line += ' </linearGradient>\n'
    svg_line += '</defs>\n'
    global_svg_file_handle.write(svg_line)
    global_fill_col = "url(#n_linear_gradient_id)"
    print(global_fill_col)
    


def start(start_filename):
    global global_svg_file_handle
    global global_svg_filename
    global_svg_filename = start_filename
    global_svg_file_handle = open(global_svg_filename, "w")
    global global_fill_col
    global_fill_col = '#ffffff';
    global global_fill_opacity
    global_fill_opacity = 1;
    global global_line_col
    global_line_col = '#000000';
    global global_line_opacity
    global_line_opacity = 1;
    global global_line_width
    global_line_width = '1px';
    global global_units_multiplier
    global_units_multiplier = 1
    global global_font_family
    global_font_family = "Times New Roman"    
    global global_font_style
    global_font_style = "normal"
    global global_font_weight
    global_font_weight = "normal"    
    global global_font_size
    global_font_size = 12;
    global global_path_relative
    global_path_relative = 0
    global global_path_x0
    global_path_x0 = 0
    global global_path_y0
    global_path_y0 = 0
    global global_arrow_angle
    global_arrow_angle=60
    import random
    import math
    
        
def finish(print_flag = 0):   
    svg_line='</svg>'
    global_svg_file_handle.write(svg_line)
    global_svg_file_handle.close()
    print("Please wait for Inkscape to open")
    if print_flag==1:
        #open and read the file
        svg_file_handle = open(global_svg_filename, "r")
        print(svg_file_handle.read())
        svg_file_handle.close()

        
def old_finish():
    svg_line='</svg>'
    global_svg_file_handle.write(svg_line)
    global_svg_file_handle.close()
    print("Please wait for Inkscape to open")
    #open and read the file:
    svg_file_handle = open(global_svg_filename, "r")
    print(svg_file_handle.read())
    svg_file_handle.close()


def display():
    import os
    os.startfile(global_svg_filename)
    



def main():
    import random
    import math
    filename = "lines.svg"
    start(filename)
    # units('cm')
    page_size(300,200)
    line_col('#000000')
    line_width(2)
    x1=50
    x2=200
    line(x1,50,x2,50,4,0)
    line(x1,100,x2,100,0,5)
    line(x1,150,x2,150,6,7)
    ## fill_col('#ddffff',1)
    # rect(10,10,180,80,2,2)
    finish(1)
    display()
    
    

if __name__=="__main__":
    main()



