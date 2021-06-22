

# Draw an eight week calendar
# starting from the date given on the line
# similar to this: date = datetime(2021,3,29)
# This should be a monday
# Here we have 29/3/2021
# See below in program

# Note that you have to install array and datetime before running this program
# Go to command prompt (in folder, press shift and right click mouse
# select "Open command window here";
# Type in command: pip install array
# Type in command: pip install datetime


# Change the date below!!!!


from array import *
from ifm import *
from datetime import timedelta, datetime



# Add notes to add to calendar here (with dates)
# examples are birthdays, anniversaries, etc
def extra(ex):
    diary = {
        "2512" : "Christmas",
	"0708" : "*Harry (2002)",
	"1107" : "*Emily (1991)",
	"1904" : "*Paul (1986)",
	"2001" : "MOT Car",
    	"0601" : "*Mum's birthday",
        "2609" : "*Dad's birthday"
    }
    x = diary.get(ex, "")
    return x


   

# This is date changed each time ############
#
date = datetime(2021,3,29)
#
# date = datetime(Year,month,day)
#
# Note that it should be a Monday ###########



filename = "calendar.svg"
start(filename)
# line_width(2)
units('cm')
line_width(0.04)
page("A4", 1)
line_col('#000000')
fill_col('none',0)

noc=7   # Number of columns
nor=8   # Number of rows
woc=3.6  # width of columns
hor=2.2  # height of rows
lm=2.375  # left margin
tm=2.0     # top margin
cell_tm = 0.6 # Inside cell top margin (for date)
cell_lm = 0.3 # Inside cell left margin (for date)

y1 = tm
y2 = tm + nor*hor
for a in range(noc+1):
    x = lm + a*woc
    line(x,y1,x,y2)

x1 = lm
x2 = lm + noc*woc
for b in range(nor+1):
    y = tm + b*hor
    line(x1,y,x2,y)




dday = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
dmon = ["January", "February", "March","April","May","June","July","August","September","October","November","December"]



fill_col('black')
line_width(0.0001)
font("Times New Roman",14)

for w in range(len(dday)):
    xpos = lm + 0.5*woc + w*woc
    middle_print(dday[w],xpos,1.45)


font("Times New Roman",13)    





date -= timedelta(days=1)
for i in range(56):
    j = i+1
    ix = i%noc
    iy = int(i/noc)
    xpos = lm + cell_lm + ix*woc
    ypos = tm + cell_tm + iy*hor
    date += timedelta(days=1)

    day = date.strftime("%d")
    month = date.strftime("%m")
    day_month = day + month
    # print(day_month)
    
    rhif_mis = int(date.strftime("%m")) - 1
    dydd1 = date.strftime("%d")
    blwydd = date.strftime("%y")
    if dydd1[0:1]=="0":
        dydd1 = dydd1[1:2]       
    if dydd1=="1" or i==0:
        t  = dydd1 + " " + dmon[rhif_mis] + " " + blwydd
        text_print(t,xpos,ypos)
        if i==0:
            testun = [t]
        else:
            testun.append(t)
        # print(str(i) + " " + testun[i])
    else:
        # t = dydd1 + " " + mis[rhif_mis]
        t = dydd1
        text_print(t,xpos,ypos)
        if i==0:
            testun = [t]
        else:
            testun.append(t) 
        # print(str(i) + " " + testun[i])
    diary = extra(day_month)
    if diary!="":
        font("Times New Roman",10)
        text_print(diary,xpos,ypos+1.4)
        font("Times New Roman",14)
    if (j%7)==0:
        print()
            
	





finish()
display()

