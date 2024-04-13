#@@@-----------------------------------------------------------------------------@@@
#
#    Turtle-Day5-1--ReusableFunctions-7Basics
#
#      using python’s turtle module to draw shapes using loops, functions,
#      and variables to draw pictures.
#
#    This demo program accomplishes the following goals:
#     - How to use an existing API library through use of online documentation
#     - Finding good API usage examples on the internet
#     - adapting examples to accomplish stated goals.
#
#    AUTHOR: Daniel Wroblewski
#    DATE/REVISON: 2/24/2024
#    STATUS: In Development
#
#    NOTE: one of *several* implicit variables on program start is __name__
#           its initial value is  '__main__'. When executed these implicit vars
#           ae set. For Python main fcn must define a function then use
#           if __name__=='__main__'  condition to execute the main() function.
#           If the python source is imported as a omdule then Python sets
#           __name__  to the module name and the if condition returns false
#           and the main method will not be executed.
#
#           More details: "python using main()"
#-----------------------------------------
#  >>>>> Modules import section  <<<<<
#
import turtle
import math
#
#  === End modules import section ===
#@@@-----------------------------------------------------------------------------@@@

# ============================================================================#
#   These functions may no longer be needed
# ============================================================================#

#
# ============================================================================#
#   The above are  functions that may no longer be needed
# ============================================================================#
#

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ---  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ---  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ---  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ---  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ---  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#
# ============================================================================#
#   General functions start here - used by many operations
# ============================================================================#
#

## -----------------------------------------------------------------------------@
#  Function getCommentLevel
#
#   Setup the comment level for entire program
#
#   cmtLvl - specify the comment level of 1 terse, 2 intermediate, 3 debug
#
## -----------------------------------------------------------------------------@

def getCommentLevel(cmtLvl):
    selCommentLevel=False
    cmtLvl=0
    while not selCommentLevel:
        cmtLvl=input("Select a comment level: 1=Basic (default <ENTER>)  2=Intermediate  3=Debug: ")
        print("selected: ",cmtLvl)
        if trapNonNum(cmtLvl,"",""):
            if cmtLvl in (None, "", "\n"):  # allow a default selection
                cmtLvl=1
                selCommentLevel=True
            else:
                print("comment level requested is [",cmtLvl,"] ")
                cmtLvl=0
                print("Invalid non-numeric character entered for comment level - try again")
        else:
            cmtLvl=int(cmtLvl)
            if 0 < cmtLvl > 3:
                print("The only valid comment levels are 1-3, try again")
            else:
                selCommentLevel=True

    print("Comment level is set to ",cmtLvl," continuing")
    return(cmtLvl)

## -----------------------------------------------------------------------------@
#  Function turtleSetUp:
#
#   Setup the turtle run parameters, particularly the shape and speed
#
#   t_type - specify the type of turtle, e.g. "classic"
#   t_Speed - specify the turtle speed from 1,3 (slow) 10,0 (fast,fastest)
## -----------------------------------------------------------------------------@
def turtleSetUp(t_type,t_Speed):
    turtle.shape(t_type)               # optional
    selTurtleSpeedSet=False
    t_Speed = 7                        # default invalid value
    while not selTurtleSpeedSet:
        t_Speed=input("Select a turtle speed level: 3=slow<default> 6=normal 1=slowest 0=fastest 10=fast: ")
        print("selected: ",t_Speed)
        if t_Speed in (None, "", "\n"):  # allow a default selection
            selTurtleSpeedSet = True
            t_Speed = 3
            print("Default speed of ", t_Speed, " selected, continuing")
        else:
            if trapNonNum(t_Speed,
    "Invalid non-numeric character entered for turtle speed - try again",
"turtleSpeed"):
                t_Speed = 8
            else:
                if t_Speed not in [0,1,3,6,10]:
                    print("The only valid speeds are 0,1,3,6 & 10-try again")
                    t_Speed = 9
                else:
                    selTurtleSpeedSet=True
                    turtle.speed(t_Speed)

    return(t_Speed)


## -----------------------------------------------------------------------------@
#   Function setpen:
#   reposition the pen and assign it a new color and size
#
#   psize - pen line thickness
#   pcolor - pen color
#   startx - new X position
#   starty - new Y position
## -----------------------------------------------------------------------------@
def setpen(psize,pcolor,startx,starty):
    turtle.penup()
    turtle.pen(pencolor=pcolor,pensize=psize)
    turtle.setx(startx)
    turtle.sety(starty)
    turtle.pendown()

## -----------------------------------------------------------------------------@
#  Function rePosition
#  Recenter the turtle using relative change coordinates
#
#  rePosition parameters:
#
#  X and Y can be moved independently of each other by calling the function
#   with the appropriate True/False values and also setting to 0 dimension that
#   you do not want to move.
#
#    movex - distance to move x coord from past square
#             should be a positive nonzero number to move past
#                            existing square in x
#    movey - distance to move y coord from past square
#             should be a positive nonzero number to move past
#                            existing square in y
#    x_move [True False]  True=we want to move x coordinate from current value
#    y_move [True False]  True=we want to move y coordinate from current value
## -----------------------------------------------------------------------------@
def rePosition(movex,movey,x_move,y_move):
    turtle.penup()
    xval=turtle.xcor()           # current position x,y
    yval=turtle.ycor()
    if x_move:
      turtle.setx(xval+movex)
    if y_move:
      turtle.sety(yval+movey)

## -----------------------------------------------------------------------------@
#  Function bordSize:
#
#   Select a border size for the viewport from the min,max, default return
#    bordrSize
## -----------------------------------------------------------------------------@
def bordSize(bordMin, bordMax, bordDeflt, bordrSize):
    bsize_check = False
    while not bsize_check:
        print("Type in an integer border size now from ",bordMin," to ",bordMax," <enter> for default ",bordDeflt,":   ")
        bordrSize = input()
        if bordrSize in (None, "", "\n"):
            bordrSize = int(bordDeflt)  # allow for a default for a numeric value
            print("Default bordersize set to ",bordrSize)
            bsize_check = True
        else:
            if trapNonNum(bordrSize,"Invalid non-numeric character entered for border size, try again",
                       "whitespace offset"):
                bsize_check = bsize_check
            else:
                bordrSize = int(bordrSize)
                if (bordrSize < bordMin or bordrSize > bordMax):
                    print("Value entered for border size is ",bordrSize," allowed value is ",bordMin," to ",bordMax,", try again")
                else:
                    bsize_check = True       # valid result, in-range
    return(bordrSize)

## -----------------------------------------------------------------------------@
#  Function selColor:
#
#  Inputs:  select color value result, default color, input prompt message
#  Output:  a single color for the object to draw
#
#  The entire rich list of colors available in Python Turtle can be found here:
#    https://cs111.wellesley.edu/labs/lab02/colors
#
#  We will only pick a few of them. A rich subset has been incorporated
#
#
#  An improvement to this function would be to call another function that opens
#   a new turtle window and paints samples of all the colors. We won't do that
#   now.
#
## -----------------------------------------------------------------------------@
def selColor(selectColor,defColor,promptCMsg):
    colorVal = False
    selectColor = defColor
    colorPalette=["red","tomato","green","chartreuse","blue","navy","cyan","magenta","maroon","purple","thistle",
                  "orchid","pink","hotpink","coral","plum","violet","salmon","orange","brown","peru","yellow","gold",
                  "khaki","sienna","gray","black"]
    while not colorVal:                       # loop until a valid color chosen
        print(promptCMsg)
        print()
        print("Valid colors are red,tomato,green,chartreuse,blue,navy,cyan,magenta,maroon,purple,thistle,"
              "orchid,pink,hotpink,coral,plum,violet,salmon,orange,brown,peru,yellow,gold,khaki,sienna,gray,"
              "black or <ENTER>")
        selectColor=input(promptCMsg)
# -----------------------------------------------------------------------------------------------
#       Here is how we use a minimal input to select the default color:
# -----------------------------------------------------------------------------------------------
        if selectColor in (None, "", "\n"):
            selectColor = defColor
            print("default color set to ",defColor," where color length is ", len(selectColor))
            colorVal=True
        else:
            if selectColor in (colorPalette):
                colorVal = True
            else:
                print("color value entered ",selectColor," is not one of the color palette colors. Try again")

    print("Selected color is ", selectColor)
    return (selectColor)

## -----------------------------------------------------------------------------@
#  Function trapNonNum:
#   Check a value to see if its a valid integer. If its not, we exit the program
#   this function could easily be improved. But it traps junk values and
#   prevents execution when entered by a user.
#
#   A better version would return a numeric error and allow forcing user to
#    enter a valid value.
#
#   testVal - the input value to test
#   whyBad - if the value is bad, tell us why
#   parmChecked - which paramter is checked according to the calling function
## -----------------------------------------------------------------------------@
def trapNonNum(testVal,whyBad,parmChecked):
#   testval is a string that could be anything
    try:
     # try converting to integer
       int(float(testVal))
    except ValueError:
        print(whyBad,parmChecked," exiting program")
        return True

# ============================================================================#
#   viewport functions start here
# ============================================================================#
#
## -----------------------------------------------------------------------------@
#  Function turtle_abscoords:
#
#  this function is designed to return the viewport values:
#   xl - x left, xt - x top, yb - y bottom yt  y
#     these are the writeable parts of the viewport
#   xal - x absolute viewable left
#   xar - x absolute viewable right
#   yat - y absolute top
#   yab - y absolute bottom
#   brdsz - viewport border size
#   These are visible but should not be written. We will put a border in this
#   space to clearly show the writeable part of the graphical viewport
#
#  Also set orientation dots in the corners.
#
# -----------------------------------------------------------------------------@
def turtle_abscords(xal,xar,yab,yat,xl,xr,yb,yt,brdsz):
#
#  turtle status:
#
    print("turtle screensize in screensz is {}".format((screensz:=turtle.screensize())))
    print("turtlex={} turtley={} ".format(turtlex:=screensz[0],turtley:=screensz[1]))
#
#  turtle viewport and border setup:
#
    turtle.pu()
    print("turtlex max ={} turtley max ={} ".format(turtlex:=screensz[0],turtley:=screensz[1]))
    print("turtlex and turtley minimum coordinates are 0")
    xl=0
    yb=0
    xr=turtlex
    x_right=xr
    print("X_right is ",x_right)
    yt=turtley
    print("Y top is ", yt)
    turtle.setworldcoordinates(xl,yb,xr,yt)
#
# Absolute hardcoded viewable corners are set and known now by experimentation:
#
    xal=xl-4
    xar=turtlex-2
    yab=-3
    yat=yt-2
#
# Set the border center coordinates in integers
#
    ybbordersize = brdsz
#    ytborder = yat - ybbordersize//2              - supposed to be a dimension calc not sure what it used for
#    xlborder = xal + ybbordersize//2
#    xrborder = xar - ybbordersize//2
#    ybborder = yab + ybbordersize//2
    ytborder = yat - ybbordersize
    xlborder = xal + ybbordersize
    xrborder = xar - ybbordersize
    ybborder = yab + ybbordersize

#
#  'pin' the 4 corners to verify they are viewable with dots
#
    print ("Pinning the 4 viewport corners now ")
    turtle.setx(xal)
    turtle.sety(yab)
    turtle.pd()
    turtle.dot(5,"green")
    turtle.pu()
    turtle.setx(xar)
    turtle.sety(yat)
    turtle.pd()
    turtle.dot(5,"red")
    turtle.pu()
    turtle.setx(xar)  # maxx)
    turtle.sety(yab)
    turtle.pd()

    turtle.dot(5,"green")
    turtle.pu()
    turtle.setx(xal)
    turtle.sety(yat)
    turtle.pd()
    turtle.dot(5,"purple")
    turtle.pu()

    turtle.setx(int(turtlex/2))
    turtle.sety(int(turtley/2))
#
#  return usable area for writing is the border less 1 pixel:
#    1st 4: absolute viewable
#    last 4:  writeable area with 1 pixel gap - all objects written in here
#
    yt=ytborder - 1
    yb=ybborder + 1
    xl=xlborder + 1
    xr=xrborder - 1

    return(xal,xar,yab,yat,xl,xr,yb,yt)

#
# ============================================================================#
#   border functions start here
# ============================================================================#
#

# -----------------------------------------------------------------------------@
#  Function draw_border:
#  Viewport border drawing and coordinate calculations
#
#  Draw out a border for the viewport that the objects should stay
#   within and return the inner calculated values of the effective viewport
#   Draw a border for user visual cue where objects can be written
#
# -----------------------------------------------------------------------------@
def draw_border(brdrsize,xal,xar,yab,yat,brdcolor,fill_ck):
#
# Set the border center coordinates
#
#    print("x right b4 bordersize is ",xar)
#
#  4/6/2024 2130 adjust the rounding so it works to round up if 1/2 pixel for center of line
#
    ytborderctr = int(yat - (round(brdrsize+0.5) // 2)) # viewport absolute + midline centered coordinates
    xlborderctr = int(xal + (round(brdrsize+0.5) // 2)) #  ensure accurate round-up at 0.5s
    xrborderctr = int(xar - (round(brdrsize+0.5) // 2))
    ybborderctr = int(yab + (round(brdrsize+0.5) // 2))

    ytborderotr = yat - brdrsize          # outer absolute coordinates + border width
    xlborderotr = xal + brdrsize
    xrborderotr = xar - brdrsize
#    print("x right b4 bordersize is ", xrborderotr)
    ybborderotr = yab + brdrsize

    turtle.pu()
    turtle.setx(xlborderctr)
    turtle.sety(ytborderctr)

    turtle.pd()
    turtle.width(brdrsize)
    turtle.pencolor(brdcolor)
    turtle.setx(xrborderctr)             # turtle lines are centered on the coordinates
    turtle.sety(ybborderctr)
    turtle.setx(xlborderctr)
    turtle.sety(ytborderctr)
    turtle.pu()

    print("Corners are UL ",xlborderctr,ytborderctr," UR ",xrborderctr,ytborderctr," LR ",xrborderctr,ybborderctr,
          " LL ",xlborderctr,ybborderctr," RETURN ",xlborderctr,ytborderctr)

    return(brdrsize,xlborderotr,xrborderotr,ybborderotr,ytborderotr)

#
# ============================================================================#
#   square functions start here
# ============================================================================#
#
#  Does requested square dimensions fit in the viewport within the border?
#  first, calculate the usable x and y parameters given the line length and
#   separator parameter between viewport border and the square object
#

# -----------------------------------------------------------------------------@
#
#  Function notOutOfBounds:
#
#  Determine if x and/or y are out of *writeable* viewport bounds for a square
#   when take into account the viewport border, the margin between
#   viewport border and square, and the size of the square's sides:
# if notOutOfBounds(xmin_left,xmax_right,sqrUsrX,ytop_sqr,ybottom_sqr,sqrUsrY,sqlen,sqrUsrThick,whitesp_adjust):
# -----------------------------------------------------------------------------@
def notOutOfBounds(xleft,xright,x_in,yceil,yfloor,y_in,sqlen, border):
# - <this is for user whitespace border for now not using>, bordoff):
#
    print("left valid x is ",xleft," right x max is",xright)
    if x_in < xleft or x_in > xright: return(False)
    print("floor value valid y is",yfloor," y_ceiling is",yceil)
    if y_in < yfloor or y_in > yceil: return(False)
    print("OutOfBoundsCheck Done and values are ok")
    return (True)

# -----------------------------------------------------------------------------@
#  Function ws_checkr:
#   ws_Adjust - the tweak factor to avoid overlapping border and objects
#   ws_User - the user-selectable additional space to further compress the
#              writeable space and enhance visual effect
#   ws='white space'
# -----------------------------------------------------------------------------@
def ws_checkr(ws_Adjust,ws_User,ws_Check):
    ws_Check=False

    while not ws_Check:
        ws_User=input("Select additional whitespace offset pixels from border+1 from values 0 to 9 or <ENTER> for default 0: ")
#
#  Trap default user input, modify and assign default value
#
        if ws_User in (None, "", "\n"):
            ws_User = 0   # allow for a default for a numeric value
            print("Default whitespace offset from border is set to ",ws_Adjust)
            ws_Check = True
        else:
            if trapNonNum(ws_User, "Invalid non-numeric character entered for whitespace offset, try again", "whitespace offset"):
                ws_Check=False
            else:
                ws_User=int(ws_User)
                if (ws_User < 0 or ws_User > 9):
                    print("Value entered for additional whitespace offset from border is ",ws_Adjust, " allowed value is 0 to 9, try again")
                else:
                    ws_Adjust = ws_Adjust + ws_User
                    ws_Check = True

    return(ws_Adjust,ws_User,ws_Check)

# -----------------------------------------------------------------------------@
#  Function sqr_ThickSet:
#
#   sqthick - the object thickness (line, etc) that is returned
#   sqthick_ck - loop check and verification that a valid thickness chosen
#   sqt_min - minimum object thickness
#   sqt_max - maximum object thickness
#
#  Initial min max were 1 and 15
# -----------------------------------------------------------------------------@
def sqr_ThickSet(sqthick, sqt_min, sqt_max):
    sqthick_ck=False
    while not sqthick_ck:
        print ("\n **************** ==== Starting new square ==== ******************")
        print("Enter the side thickness for square, minimum ",sqt_min," maximum ",sqt_max, " 0 to end: ")
        sqthick = int(input())
#
#   if press ENTER here the program bombs out
#
        if trapNonNum(sqthick, "Invalid non-numeric character entered for border thickness, try again","Border Thickness"):
            sqthick_ck=False
        else:
            if sqthick == 0:
                print("Program exit requested with 0 thickness input, ending execution")
                exit()
            if (sqthick < sqt_min or sqthick > sqt_max):
                print("Value entered for border thickness is ",sqthick," allowed value is ",sqt_min," to ",sqt_max," try again")
            else:
                sqthick_ck=True

    return(sqthick)

# -----------------------------------------------------------------------------@
#  Function anchor_box_test:
#
#  Inside corners:
#    xmin_left_range
#    xmax_right_range
#    ytop_sqr_range
#    ybottom_sqr_range
#    anchor_ck -  success flag
#
#    The rest of the values are hardcoded as this is a diagnostic routine
#
#    screen_erase will run when user wants it to and erase all 4
#     objects in viewport
#
#  The unique feature of this function is that it incorporates recursion to
#   "erase" the anchor boxes. This is a single recursion since nothing else
#   makes sense. The controlling variable anchor_ck that controls the recursion
#   has a special value of the background
#
# -----------------------------------------------------------------------------@
def anchor_box_test(xmin_left_range,xmax_right_range,ytop_sqr_range,ybottom_sqr_range,anchor_ck,min_length,bxcolor,turtleScreen,prtCmt):
#
#   Recursion return check:
#
    if not anchor_ck:
        printTest = True
        if (bxcolor == turtleScreen.bgcolor()):
            printTest = False                   # last recursion

        if printTest:
            print("The test starts the boxes on the whitespace border")
        #
        #  Write sides: Top, right,bottom, left - Clockwise
        #
        sideCount = 0
        for sideCount in range(4):
            if sideCount == 0:
                sqrXStart = xmin_left_range
                sqrYStart = ytop_sqr_range
                if printTest and prtCmt:
                    print("TOP-Upper left test box X-start is ", sqrXStart, " Y-start is ", sqrYStart)
            if sideCount == 1:
                sqrXStart = xmax_right_range - min_length
                if printTest and prtCmt:
                    print("RIGHT-Upper right test box X-start is ", sqrXStart, " Y-start is ", sqrYStart)
            if sideCount == 2:
                sqrYStart = ybottom_sqr_range + min_length
                if printTest and prtCmt:
                    print("BOTTOM-Upper right test box X-start is ", sqrXStart, " Y-start is ", sqrYStart)
            if sideCount == 3:
                sqrXStart = xmin_left_range  # these are trusted values to check corners
                if printTest and prtCmt:
                    if printTest:
                        print("LEFT-Lower right test box X-start is ", sqrXStart, " Y-start is ", sqrYStart)

            drawsqr(20, sqrXStart, sqrYStart, 4, bxcolor)

        if ( bxcolor == turtleScreen.bgcolor() ):   # if this is true then setup for recursion end
            anchor_ck = True                        # breakout condition for recursion end on NEXT iteration AFTER print rectangles
            return(anchor_ck)
#
#   Print one more box set-the next recursion is last one, when draw color is background color we also set the
#     recursion condition check which also happens to be the overwrite color that "erases" the anchor boxes....
#
        ack = input("Press <ENTER> to erase anchor boxes and screen")
        bxcolor = turtleScreen.bgcolor()

        anchor_ck=anchor_box_test(xmin_left_range,xmax_right_range,ytop_sqr_range,ybottom_sqr_range,anchor_ck,min_length,bxcolor,turtleScreen,prtCmt)

    else:                       # do not recurse
        return(anchor_ck)

# -----------------------------------------------------------------------------@
#  Function screen_erase:
#
#   This function "erases" all written objects within the printable screen area
#   leaving just the border and the whitespace
#
#   Was unable to figure out how to get this to work according to the documentation
#   given reasonable time.
#
def screen_erase(xmin_l_range,xmax_r_range,yt_sqr_range,yb_sqr_range,erase_ck):
    print("screen_erase: this is a stub - does nothing")
    erase_ck=True
    return(erase_ck)

# -----------------------------------------------------------------------------@
#  Function calcActualRange:
#
#   Calculate the min and max x and y coordinates for the square object
#    using the user-selected values of
#    xi_left min x left allowed
#    xa_right max x right allowed
#    yt y top coordinate allowed
#    yb y bottom coordinate allowed
#    x_il  (given) x inner left of viewport - usable value for square
#    x_ir  (given) x inner right of viewport - usable value
#    y_it  (given) y inner top of viewport - usable value
#    y_ib  (given) y inner bottom  of viewport - usable value
#    sqln  (user) square side length
#    brdthk (user) square side thickness
#    brd_offset - (user) square offset from the viewport border
#
#  This function just calculates the coordinates does not evaluate if
#   out of bounds
#
# -----------------------------------------------------------------------------@
def calcActualRange(xi_left,xa_right,yt,yb,x_il,x_ir,y_it,y_ib,sqln,brdthk,brd_offset):
    xi_left = x_il + brdthk + brd_offset
    xa_right = x_ir - brdthk - sqln - brd_offset
    yt = y_it - brdthk - brd_offset
    yb = y_ib + brdthk + sqln + brd_offset

    return(xi_left,xa_right,yt,yb)

# -----------------------------------------------------------------------------@
#  Function drawsqr
#
#   function to actually draw the square after all bounds and values
#    tests are successful
#
# -----------------------------------------------------------------------------@
def drawsqr(len,x,y,bordwid,sq_color):
  print("Side length ",len," Starting x:",x," starting y: ",y," border width: ",bordwid," Square color: ",sq_color)
  turtle.pu()
  turtle.pencolor(sq_color)
  turtle.width(bordwid)
  turtle.setx(x)
  turtle.sety(y)
  turtle.pd()
  for t_obj in range(4):
    turtle.forward(len)          # 4/7 2100 - changed direction from 'backward' to 'forward' and -90 to +90 now off
    turtle.right(90)             # prints downward not upward
  turtle.pu()

#
#============================================================================#
#   Line functions start here
#============================================================================#
#
# -----------------------------------------------------------------------------@
#  Function lineattribs:
#
#   Setting the line width and color and out of bounds check:
#
# -----------------------------------------------------------------------------@
def lineattribs(turtleLine,lcolor,lwidth,lwmin,lwmax):
    lcolor = input("Enter a primary color for line:  ")

#    lwidth = int(input("Enter a width for line from ",lwmin," to ",lwmax,", 0 to quit: "))
    print("Enter a width for line from ",lwmin," to ",lwmax,", 0 to quit: ")
    lwidth=int(input())

    if linewidth >= lwmin and linewidth <= lwmax:
     turtleLine.width(lwidth)
     turtleLine.pencolor(brdcolor)
     return 0
    elif linewidth == 0:
     print("Line printing halted")
     return 2
    else:
     print("Line thickness out of bounds-valid range is ", lwmin, " to ", lwmax)
     return 1

# -----------------------------------------------------------------------------@
#  Function drawline:
#
#   Lines can be drawn at any angle as long as they stay within the viewport
# -----------------------------------------------------------------------------@
def drawline(x, y, x1, y1):
    turtle.pu()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.setx(x1)
    turtle.sety(y1)
    turtle.pu()

# -----------------------------------------------------------------------------@
# Function reportWhichBoundExceeded
#
#  If line parameters for x and y start or end point are out of the viewport and overlap
#  border then report a failure. This currently does not correct for line width
#
# -----------------------------------------------------------------------------@
def reportWhichBoundExceeded(x_irright, x_inleft, y_intop, y_inbottom, sqx, sqy, sqx1, sqy1):
    stringExceed = ""
    if sqx - border <= x_inleft or sqx - border >= x_irright: stringExceed = "x-point1"
    if sqy - border <= y_inbottom or sqy - border >= y_intop: stringExceed = stringExceed + " y-point1"
    if sqx1 + sqlen + border >= x_irright or sqx1 - border >= x_irright: stringExceed = stringExceed + " x-point2"
    if sqy1 + sqlen + border >= y_intop or sqy1 - border >= y_intop:  stringExceed = stringExceed + " y-point2"
    return (stringExceed)


#============================================================================#
#   start of core program
#============================================================================#
#
#  Step 2:
#  Once the square is drawn, change its color.
#   Then make the line thicker.
#   (pensize or width)
#
#   Change the speed the turtle draws at.
#

print("Welcome to Turtle Day5 Basics")
print("-----------------------------")

turtle.shape("classic")                               # optional
turtleSpeed=6                                         # 0 is fastest
turtleSpeed=turtleSetUp("classic",turtleSpeed)
turtle.speed(turtleSpeed)

# ------------------------------------------------------------------------------------------------------------
#   Balance noise redux vs debugging and allow tweaking of debugging comments in individual
#    modules at different detail levels
# ------------------------------------------------------------------------------------------------------------

cmtLevel=0
cmtLevel=getCommentLevel(cmtLevel)

bordersize=4
BORDERMINSIZE=1
BORDERMAXSIZE=10
bordersize=bordSize(BORDERMINSIZE,BORDERMAXSIZE,bordersize,bordersize)      # min,max,default,border size
bordercolor = "blue"
bordercolor=selColor(bordercolor,"blue","Pick a border color now: ")

x_absleft=0             # Physical boundaries of viewport
x_abs_rt=0
y_abs_bottom=0
y_abs_top=0
x_left=0                # used for telling user the writeable inner dimensions
x_right=0
y_bottom=0
y_top=0

# ------------------------------------------------------------------------------------------------------------
# 1st 4 are viewable absolute limits last 4 are usable for writing objects including
#  viewport border
# ------------------------------------------------------------------------------------------------------------

coords=turtle_abscords(x_absleft,x_abs_rt,y_abs_bottom,y_abs_top,x_left,x_right,y_bottom,y_top,bordersize)

# ------------------------------------------------------------------------------------------------------------
#  The viewport coordinates are now determined, saving next:
# ------------------------------------------------------------------------------------------------------------

x_absleft=coords[0]    # viewport absolute viewable boundaries
x_abs_rt=coords[1]
y_abs_bottom=coords[2]
y_abs_top=coords[3]
x_left=coords[4]       # tell user the writeable inner dimensions
x_right=coords[5]      # these 4 primarily used for debugging and reminder of abs viewport dimns
y_bottom=coords[6]
y_top=coords[7]

if (cmtLevel==3):
    print("These are the absolute values of the viewport:")
    print("The absolute coord values of xabs,xtop,xabstop,yabsbottom,yabstop are",x_absleft,x_abs_rt,y_abs_bottom,y_abs_top)
    print("The writeable coord values of xleft,xright,ybottom, ytop are",x_left,x_right,y_bottom,y_top )

# ------------------------------------------------------------------------------------------------------------
#   return inner dimension of writeable space
#
#   The border is drawn as a visual aid and also to start determining actual coordinates so we do not
#   overwrite the screen and/or cause object wrapping.
# ------------------------------------------------------------------------------------------------------------

viewport=draw_border(bordersize,x_absleft,x_abs_rt,y_abs_bottom,y_abs_top,bordercolor,False)
x_innerright=0
x_innerleft=0
y_innerbottom=0
y_innertop=0
x_innerright=viewport[2]    #  these 4 are inner dimensions adjusted for border thickness - inside borders
x_innerleft=viewport[1]
y_innertop=viewport[4]
y_innerbottom=viewport[3]
if (cmtLevel==3):
    print("The inner dimensions of viewport adjusted for border no pixel gap is now: border size, xleft,xright,ytop,ybottom are:",
      bordersize,x_innerleft,x_innerright,y_innerbottom,y_innertop)

# ------------------------------------------------------------------------------------------------------------
#  Writeable area adjustments and testing
#   need odd/even test for bordersize to adjust dimensions
# ------------------------------------------------------------------------------------------------------------

anchor_ck=False
anchor_len=20
yt_adj=y_top
xl_adj=int(x_left)
xr_adj=int(x_right)

yb_adj=y_bottom
if (cmtLevel==3):
    print("round bordersize +.5 // 2: ",round(bordersize+0.5)//2,"bordersize // 2: ",bordersize//2)

# ------------------------------------------------------------------------------------------------------------
#  Bordersize odd number check/adjust dimensions - require rounding
# ------------------------------------------------------------------------------------------------------------

if not round(bordersize+0.5)//2 == bordersize//2:
    xl_adj=xl_adj+1
    print("x_left is ",x_left," xl_adj is ",xl_adj)
    yt_adj=y_top-2
    xr_adj=xr_adj
    yb_adj=yb_adj+1
# -----------------------------------------------------------------------------------------------------
#  The anchor device is a diagnostic to show that the program is running within the border and
#   shows pixel-level resolution. The gap between the border and the green diagnostic boxes should
#   be exact, or within 1 pixel of the horizontal and vertical border lines. This can be affected by
#   monitor hardware resolution and display card among other things even if the calculations are right.
#   The same can be said with the x:y display ratio and there may be unknown issues with Python Turtle
#   affecting display as well which may manifest with larger objects.
# -----------------------------------------------------------------------------------------------------
anchor_ans="X"
anchor_ck=False          # leave it to this if never run a check
anchor_ans=input("Do you want to check and adjust viewport writeable area - Y to proceed: ")
anchor_ans=anchor_ans.upper()
turtlescr=turtle.getscreen()
#clearcolor=turtlescr.bgcolor()

if anchor_ans == "Y":
    anchor_ck=anchor_box_test(xl_adj,xr_adj,yt_adj,yb_adj,anchor_ck,anchor_len,"green",turtlescr,cmtLevel)
#    if anchor_ck:
#        ack = input("Press <ENTER> to erase anchor boxes and screen")
#        turtlescr=turtle.getscreen()
#        clearcolor=turtlescr.bgcolor()
#        anchor_ck = anchor_box_test(xl_adj, xr_adj, yt_adj, yb_adj, anchor_ck, anchor_len, clearcolor, "erase")

#
#   Set the finalized inner dimensions. Note that objects min/max may need to be set so that the max
#    object width does not exceed the boundaries to avoid overwriting margins
#
if (cmtLevel==2):
    print("draw_border x_innerleft: ",x_innerleft," x_innerright ",x_innerright," y_innertop: ",y_innertop," y_innerbottom: ",y_innerbottom)
x_innerleft=xl_adj
x_innerright=xr_adj
y_innertop=yt_adj
y_innerbottom=yb_adj
if (cmtLevel==3):
    print("Reset inside boundaries to:  x_innerleft: ",x_innerleft," x_innerright ",x_innerright," y_innertop: ",
       y_innertop," y_innerbottom: ",y_innerbottom)
#
#  Drawing a square, calculating the values then loop around again until no more squares wanted
#
#  Enforce reasonable square thickness values:
#
SQTHICKMIN = 1            # Constants: fixed allowable square thicknesses
SQTHICKMAX = 15
DEFCOLOR="blue"           # default object color
sqcount=0                 # count of number of squares created
closeVP=0                 # At the end of this we CLOSE the ViewPort or move to next object type
sqloop = 0                # Square Loop - on exit finished drawing current square
sqrUsrColor=DEFCOLOR
while closeVP==0:            # when not true/done with squares we want to close the current viewport/next object type
    while sqloop == 0:       # we want to create another square while 0/false and create it when inputs are not trash
        traptrash = 0            # rerun the user inputs until valid then print the square
        sqcolor = DEFCOLOR     # reset the color
        while traptrash==0:       # reset selected values and inputs on a retry
            sqrUsrX = 0           # user inputs for starting x y of square
            sqrUsrY = 0
            max_len = 0          # calculated max and min side lengths
            min_len=0            # calculated min side length based on side thickness + 1
            sqlen = 0             # Square values: side length, side thickness
            sqrUsrThick = 0
            maxside = 0           # upper limit of side length after coordinates chosen
            xmin_left = 0         # corner values of square - min, max X & Y  range
            xmax_right = 0
            ytop_sqr = 0
            ybottom_sqr = 0
            print ("\n **************** ==== Starting new square ==== ******************")
# ---------------------------------------------------------------------------------------------------
#  User inputs square thickness and program sets a square-specific viewport boundary set:
# ---------------------------------------------------------------------------------------------------
            sqrUsrThick=sqr_ThickSet(sqrUsrThick,SQTHICKMIN,SQTHICKMAX)
            print("Side thickness sqrUsrThick selected is ",sqrUsrThick)
            x_innerleft_sq = x_innerleft + sqrUsrThick
            x_innerright_sq = x_innerright - sqrUsrThick
            y_innertop_sq = y_innertop - sqrUsrThick
            y_innerbottom_sq = y_innerbottom  + sqrUsrThick

# ====================================================================================================
#          Alignment device
#
#                   < sq thickness bounds rational test
#               < bad no-numeric value
#           < sqthick_ck
#       < traptrash
#   < sqloop - write another one ?
#< viewport closeout (left margin)
# ====================================================================================================

# ---------------------------------------------------------------------------------------------------
#    max_len is determined by x and y position selections along with right / top-y border vs
#       absolute min margin adjusted by the 2*sqrUsrThick and the 1 pixel.
#
#       x: writeable area to the right border is abs right pixel - border - whitespace
#            for writeable space only for use input
#            writeable area margins must be separately calculated on both left and right, using
#            1x for border and 1x for whitespace in each dimension.
#
#       y: the leg of the square descends down, clockwise. So the upper limit is top pixel# minus
#            writeable area margins. Must be separately calculated on both top and bottom, using
#            1x for border and 1x for whitespace in each dimension.
#
#       Do we want to bother the end user with absolute values or just offsets from left and top writeable
#        areas? The latter makes more sense then translate into actual pixel locations.
#
# ---------------------------------------------------------------------------------------------------
#
#   Next must get the start x and start y - these dictate the
#    length of the side
#
#   Calculate the min x, max x, min y, max y coordinate boundaries range we can use
#    as the square starting point based on the side length
#
#   The square start and end points must fit between these dimensions:
#
#    xmin_left to xmax_right and ybottom_sqr to ytop_sqr
#    or must be reported as out of bounds and try again
#
#   The xmax_right_range and ybottom_sqr_range are adjusted to allow for a
#    minimum side length of 2*sqrUsrThick + 1 pixel inside the square or its a box not a square.
#    Given this, it will not be possible to underrun min size length. Side max length will be
#    restrained later when user selects the x and y start coordinates
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
#   Transfer the viewport + object thickness to a new variable set
# ---------------------------------------------------------------------------------------------------
            xmin_left_range = x_innerleft_sq
            ytop_sqr_range = y_innertop_sq
# ---------------------------------------------------------------------------------------------------
#       Square side length check and accept:
#       -----------------------------------------
#   4/6/2024:  User inputs side value length
#              The user has to enter a length and a starting y then we have to check to see if that is allowable
#               > We tell the user to select length from a valid possible range
#               Then in next section we give them a set of starting Xs and Ys they are allowed to select from.
#
#               We should also give them the option to wipe the screen -do later-
#
#               ** min_len must be at least 2x side thickness plus 1 pixel -1 or more spaces inside of square- **
#
#   4/6/2024:
#          we cannot get these yet because we do not know the user selected length
#
#           xmax_right_range = x_innerright_sq - *user length*
#           ybottom_sqr_range = y_innerbottom_sq  *user length*
#
#            max_side available to user  to choose is:
#             y_innertop_sq =  y_innertop - sqrUsrThick
#             y_innerbottom_sq = y_innerbottom  + sqrUsrThick
#             leaving max side to be  =y_innertop - y_innerbottom_sq
# ---------------------------------------------------------------------------------------------------
            max_side = y_innertop_sq - y_innerbottom_sq  # largest possible side based on available y range-limiting
            min_len = 2 * sqrUsrThick + 1                 # minimum length of sides must be this for a valid non-box square
            max_len=y_innertop_sq - y_innerbottom_sq
            sqr_userSelectLen=0
            userlen_ck=False              # loop variable proving user selected length in valid range
            while not userlen_ck:
                print("Select a side length not including the thicknesses.The options are ",min_len," to ",max_len)
                sqr_userSelectLen=int(input())
                if trapNonNum(sqr_userSelectLen, "Invalid non-numeric character entered for square length - try again","square length"):
                    userlen_ck = False
                else:
                    if sqr_userSelectLen < min_len or sqr_userSelectLen > max_len:
                        print("Square length chosen is ",sqr_userSelectLen," the allowable values are ",min_len," to ",max_len," try again")
                    else:
                        userlen_ck=True

            print("The selected length is ",sqr_userSelectLen," within allowable range of ",min_len," to ",max_len)
# ---------------------------------------------------------------------------------------------------
#      4/6/2024:  with the side length we can calculate the available starting x and y coordinates....
#
#         configured top y:  y_innertop_sq
#         requested bottom y: y_innerbottom_sq + sqr_userSelectLen
#                      if range bottom > top  or right < left then a logical error
#                      if bottom = top  and/or left=right then
#                       - the starting y is y_innertop_sq <max sized square possible>
#                       - if left=right then the length is too long and y would be out of range (bottom > top)
#                 otherwise
#                      y_bottom_coord = (y_innerbottom_sq + sqr_userSelectLen) to y_top_coord <= y_innertop_sq>
#         If y is successful then x will be as well so now we calculate the allowable x coords and will be no
#            bottom < top <but can check for it>
#                      x_left_coord=x_innerleft_sq
#                      x_right_coord=x_innerright_sq - sqr_userSelectLen
#
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
#       X and Y user-selectable coordinates
#
#   4/6/2024:  Now that we know the user selected side length and verified its within min and max
#               range of available lengths we can calculate the available x and y coordinates
#               user can pick from for X and Y coordinates
# ---------------------------------------------------------------------------------------------------
            ytop_sqr_range = y_innertop_sq
            ybottom_sqr_range = y_innerbottom_sq + sqr_userSelectLen
            xmin_left_range = x_innerleft_sq
            xmax_right_range = x_innerright_sq - sqr_userSelectLen
# ---------------------------------------------------------------------------------------------------
#       Y bounds and values check and accept:
# ---------------------------------------------------------------------------------------------------
            if ybottom_sqr_range > ytop_sqr_range:     # no values possible exceeded possible length - logic failure
                print("Y bounds exceeded, exiting with lowerbound of ",y_lowerbound," and y_upperbound of ",y_upperbound)
                print("Program failure - contact support")
                exit()
            else:
                if ybottom_sqr_range == ytop_sqr_range:          # only one possible value
                    sqrUsrY = ytop_sqr_range
                else:                                     # multiple coord values possible - y
                    input_y_ck=False
                    while not input_y_ck:
                        print("Y values available are ",ybottom_sqr_range," to ",ytop_sqr_range," choose in range now")
                        sqrUsrY=int(input())
                        if trapNonNum(sqrUsrY, "Invalid non-numeric character entered for","Y position"):
                           input_y_ck=False
                        else:
                            if sqrUsrY >  ytop_sqr_range or  sqrUsrY < ybottom_sqr_range:
                                print("User Y value selected is ",sqrUsrY, " which is out of bounds of ",ybottom_sqr_range,
                                      " to ",ytop_sqr_range," try again")
                            else:
                                print("User selected ",sqrUsrY, " as Y value - valid value, in range of ",
                                      ybottom_sqr_range," to ",ytop_sqr_range)
                                input_y_ck = True
# ---------------------------------------------------------------------------------------------------
#       X bounds and values check and accept:
# ---------------------------------------------------------------------------------------------------
            xmin_left_range = x_innerleft_sq
            xmax_right_range = x_innerright_sq - sqr_userSelectLen
            if xmax_right_range < xmin_left_range:                          # no values possible exceeded possible length
                print("X bounds exceeded, exiting with X left value of ", xmin_left_range,
                    " and X right value of ", xmax_right_range)
                print("Program failure - contact support")
                exit()
            else:
                if xmax_right_range == xmin_left_range:                 # only one possible value
                    sqrUsrX = xmin_left_range
                else:                                            # multiple values possible - x
                    input_x_ck = False
                    while not input_x_ck:
                        print("X values available are ", xmin_left_range, " to ", xmax_right_range," choose in range now ")
                        sqrUsrX = int(input())
                        print("X value chosen on input is ",sqrUsrX)
                        if trapNonNum(sqrUsrX, "Invalid non-numeric character entered for", " X position"):
                            input_x_ck = False
                        else:
                            print("User selected ",sqrUsrX, " as X value")
                            if sqrUsrX > xmax_right_range or sqrUsrX < xmin_left_range:
                                print("User selected ",sqrUsrX, " as X value which is out of bounds of ",xmin_left_range,
                                        " to ", xmax_right_range, " try again")
                            else:
                                input_x_ck = True
                                traptrash=1                  # breaks out of the input looks and prints square

            print("X value chosen: ",sqrUsrX," Y value chosen: ",sqrUsrY," length chosen: ",sqr_userSelectLen)
            print("X and Y values are selected and are in range, proceeding to select color & draw square")
# ====================================================================================================
#     Alignment device:
#           < length and bounds checking
#       < traptrash
#   < sqloop - write another one ?
# < viewport closeout (left margin)
# ====================================================================================================

        sqrUsrColor = selColor(sqrUsrColor, "green", "Pick a square border color now: ")

        print("Summary of Ranges, Values selected: ")
        print("xmin_left_range=", xmin_left_range, " xmax_right_range=", xmax_right_range," X start sqrUsrX ",sqrUsrX)
        print("ybottom_sqr_range=", ybottom_sqr_range,"ytop_sqr_range=", ytop_sqr_range," Y start sqrUsrY=",sqrUsrY)
        print("sqr_userSelectLen side length=", sqr_userSelectLen, "sqrUsrThick=", sqrUsrThick)
# ---------------------------------------------------------------------------------------------------
#   For now we are not adding user selectable whitespace boundaries - the goal is to have a 1 pixel
#    correctly calculated effective viewport drawing window.
#
#, "whitesp_adjust=", whitesp_adjust)
# ---------------------------------------------------------------------------------------------------
        if notOutOfBounds(xmin_left_range,xmax_right_range,sqrUsrX,ytop_sqr_range,ybottom_sqr_range,sqrUsrY,sqr_userSelectLen, sqrUsrThick):
#,whitesp_adjust):
            print("Drawing square now")
            drawsqr(sqr_userSelectLen,sqrUsrX,sqrUsrY,sqrUsrThick,sqrUsrColor)
            sqcount += 1                                            # Increment the number of squares drawn
        else:
            print("Parameters exceed viewport size, try again")
            print("the starting X position ",sqrUsrX," must be greater,equal than ",x_innerleft," and less than ",
              x_innerright - sqlen - 2 * sqrUsrThick)
# - 2 * whitesp_adjust)
            print("the starting point of ", xmin_left_range, " allows for a max length of ", maxside, " and ",sqr_userSelectLen,
              " was requested")
            print("the starting Y position",sqrUsrY, " must be greater than ", ybottom_sqr_range, "and less than ",
              ytop_sqr_range)
#- 2 * whitesp_adjust)
            print("the starting point of ",sqrUsrY," allows for a max length of ",maxside," and ",sqr_userSelectLen," was requested")

# ========================================================================================================
#     Alignment device:
#           < length and bounds checking
#       < traptrash  - the above is good ready to draw square
#   < sqloop - write another one ?
# < viewport closeout (left margin)
# =========================================================================================================

#print("Click to close turtle viewport")
#turtle.Screen().exitonclick()
x=input("Press any key to clear the screen for next object drawing")
turtle.clearscreen()
print("Moving on to line drawing in new turtle viewport")

exit()

#  ===================================================================================
#
#   STEP 1: Draw a line
#            Step 1. Draw a line
#
#  ===================================================================================
#
#  for sake of simplicity we hardcoded the linewidth values at
#    and users must enter in valid primary color choices:
#
LoopLine=True
lwidthmin=1
lwidthmax=20
while LoopLine:
  print("\n   Lets draw one line")
  print("-----------------------------")
  x,y = int(input("Type first XY point,0 and 0 to skip line"))
  if not (x==0 and y==0):
    x1,y1 = int(input("Type second XY point"))
    if notOutOfBounds(x_innerright,x_innerleft,y_innertop,y_innerbottom,x,y,x1,y1):
      lineresult = lineattribs(linecolor,linewidth,lwidthmin,lwidthmax)
      if lineresult < 1:
        drawline(x,y,x1,y1)
        LoopLine=False
    else:
     stExceed=reportWhichBoundExceed(x_innerright,x_innerleft,y_innertop,y_innerbottom,x,y,x1,y1)
     if len(stExceed) > 0:
      print("The following bounds were exceeded",stExceed)
     else:
      print("Invalid condition for point out of bounds",x,y,x1,y1)

#
#  Step 3
#  Draw two squares side by side that do not touch; set the turtle speed to 0 first
#
#


#
#  Create a square function.
# - take the length of each side as a parameter
# - draw square using the turtle
# - Call this function instead of the lines you used
#    to draw the squares in the prior two steps.
#    RECOMMENDED: Use a loop
#

#
#   STep 5: Create a rectangle function
#    Takes width and height
#
#
#   Step 6: Draw a picture using a FOR loop that calls rectangle or square
#            Try to include at least one rectangle and one square
#            No user input is allowed!
#

#
#   Step 7:
#     Create a program house.py that has the following functions:
#      - square: takes the length of a side as a parameter and draws a square
#                 (each interior angle is 90 degreed)
#      - Triangle: takes the length of a side as a parameter and draws an equi
#                   lateral trinagle  (each exterion turn is 120 degrees)
#      - house: takes the length of a line as a parameter and draws a house by
#                calling your triangle and square functions
#
#    Square and triangle functions must use a FOR loop.
#    Test your function by drawing houses of different sizes.
#
# Next, create a program stop.py that has the following functions:
#     • rectangle: takes the width and height as parameters and draws a rectangle
#                   (each interior angle is 90°)
#     • octagon: takes the side length as a parameter and draws an octagon (each
#                   exterior turn is 45°)
#     • stop: takes the octagon side length as a parameter and draws
#             a stop sign by calling octagon,moving forward 3/8 of the side
#             length, and drawing a rectangle sign post that is 1/5 of the side
#             wide and has a height that is double a side.
#
#  Note that your shape functions must use a for loop. Test that your functions
#   are working by drawing multiple stop signs of different sizes. For example:
#
#   (see PDF document for the graphics)
#
#  Celebrate your progress!
#
#    Take a screenshot of your drawing and share it in the group:
# •   Mac: http://www.wikihow.com/Take-a-Screenshot-in-Mac-OS-X
# •   Windows: http://www.wikihow.com/Take-a-Screenshot-in-Microsoft-Windows
#
#






#
#  next step is to create a triangle function
#
#  now draw a picture using a for loop that calls rectangle or square. The picture
#   should include at least one rectangle and one square without any user input.
#
#  create a house.py program: draws a rectangle, draws a triangle; takes the length
#    of a side as a parameter and draws an equilateral triangle. (each turn 120 degrees)
#    Then take the length of the line as a parameter nd draws a house by calling your
#    triangle and square functions. The square and triangle functions must use a for
#    loop. draw houses of different sizes.
#
#  Next, create a program stop.py that has the following functions:
#    - rectangle
#    - octagon (45 degree angles)
#    - takes the octagon side length as a parameter and draws a stopsign
#       by calling octagon, moving forward 3/8 of the side length, drawing the
#       a rectangle signpost that is 1/5 of the side wide  and has a height that is
#       double a side. The shape function *must use* a FOR loop.
#
#  final step is to draw houses.
#
#



exit()

#============================================================================#
#============================================================================#
#   END of core program
#============================================================================#
#============================================================================#

#
#
#  >>>>>>>>>>>>>>>> this is the old code, that follows below
#  >>>>>>>>>>>>>>>>>   it should eventually be discarded but useful for samples
#
#
#

#
#   Orient the screen with dimensional markers to know the dimensional parameters
#
#turtle.listen(1,1)
#turtle.setworldcoordinates(xlborder, ybborder, xrborder, ytborder)
#setpen(3,"blue",xlborder,ytborder)
#turtle.setx(0.9*xlborder)
#turtle.sety(0.9*ytborder)
#turtle.pd()
#turtle.setx(xrborder)
#turtle.sety(ytborder)
#turtle.sety(ybborder)
#turtle.setx(xlborder)
#turtle.sety(ytborder)
#turtle.pos(xrborder,ytborder)
turtle.pu()
#turtle.forward(turtlex - 2*offset)

#
#  draw dot in center
#
#screenxy=turtle.screensize()
#print("screenyx is",screenxy)
#turtle.home()
#turtle.dot(20,"red")
#print("Done with turtle painting now! Click on the Turtle screen to exit")
#turtle.Screen().exitonclick()
#exit()

#MAXX=140
#MINX=-140
#MAXY=190
#MINY=-190
#sq_shape=shape("square")   shape applies to the turtle object
#print("Welcome to Turtle Day5 Basics")
#print("-----------------------------")
#print("Valid entry values are:")
#print("x:  -140 to + 140-side length ")
#print("y:  -190 to + 190-side length ")
#print("Line thickness values 1-30")
#print("Side lengths from 2 to 100")
#print("Colors:  red green blue yellow black purple")

#sqcolor=input("Enter the square's color: ")
#if sqcolor not in ("red","green","blue","yellow","black","purple"):
#    print("Invalid color try again")
#    exit(-1)

#sidesz=input("Enter the square's side length: ")
#if trapNonNum(sidesz,"Invalid non-numeric character entered for"," square side length"):
# exit(-1)
#sidesz=math.ceil(float(sidesz))
#if sidesz not in range(2,100):
#    print("Invalid side length try again")
#    exit(-1)

#sqx=input("Enter the square's x position lower corner: ")
#if trapNonNum(sqx,"Invalid non-numeric character entered for"," starting X position"):
# exit(-1)

#sqx=math.ceil(float(sqx))
#testsizeX=sqx + sidesz

#if ( testsizeX > MAXX or sqx < MINX ):
#    print("Invalid X start position, try again")
#    exit(-1)

#sqy=input("Enter the square's y position lower corner: ")
#if trapNonNum(sqy,"Invalid non-numeric character entered for"," starting Y position"):
# exit(-1)

#sqy=math.ceil(float(sqy))
#testsizeY = sqy + sidesz
#if ( (testsizeY > MAXY) or (sqy < MINY) ):
#    print("Invalid Y start position, try again")
#    exit(-1)

#sqpenwidth=input("Enter the square's line thickness: ")
#if trapNonNum(sqpenwidth,"Invalid non-numeric character entered for"," pen width"):
# exit(-1)
#
#  Check pen thickness vs side size
#
#sqpenwidth=math.ceil(float(sqpenwidth))
#if 2*sqpenwidth > sidesz:
#   print("Pen width cannot exceed half of side size, try again")
#   exit(-1)
#else:
#
#   assumption is line thickness is is divided equally between left
#     and right, above and below, pen coordinates so we do not want to
#     draw outside the viewport
#
#  penthick=math.ceil(sqpenwidth/2)
#  if ( penthick + sqx > MAXX):
#    print("Pen width plus X start point exceed viewport size, try again")
#    exit(-1)
#  elif ( penthick + sqy > MAXY):
#    print("Pen width plus Y start point exceed viewport size, try again")
#    exit(-1)

#turtle.listen(1,1)
#setpen(sqpenwidth,sqcolor,sqx,sqy)
#
#offsetx=0
#offsety=0
#print("Do you want to move X for next square?")
#tfx=bool(input())
#if tfx:
#    print("How much?")
#    offsetx=input()
#print("Do you want to move Y for next square?")
#tfy=bool(input())
#if tfy:
#    print("How much?")
#    offsety=input()
#
# draw first square, move turtle, draw second square
#
#drawsqr(sidesz)
#
# def recenterX(linelenX,linelenY,sizex,sizey,movex,movey,x_move,y_move):
#
#recenterX(sidesz,sidesz,sqpenwidth,sqpenwidth,tfx,tfy,offsetx,offsetx)
#drawsqr(sidesz)

#turtle.home()
#print("Done with turtle painting now! Click on the Turtle screen to exit")
#turtle.Screen().exitonclick()
#
#
#



