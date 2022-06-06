from turtle import *
#First color is pencolor second is fillcolor.
color('black', 'yellow')
speed(0)

continue_x = True
while continue_x:
    #head shape
    #----------
    home()
    begin_fill()
    fillcolor('#FFEF00')
    circle(160,360)
    end_fill()
    penup()
    #cheeks
    #------------
    goto(90,70)
    pendown()
    begin_fill()
    fillcolor('#FC6C85')
    circle(40,360)
    end_fill()
    penup()
    goto(-90,70)
    pendown()
    begin_fill()
    fillcolor('#FC6C85')
    circle(40,360)
    end_fill()

    #right eye
    #------------
    penup()
    goto(70,130)
    pendown()
    begin_fill()
    fillcolor('#ffffff')
    circle(50,360)
    end_fill()
    penup()
    goto(70,180)
    pendown()
    dot(30)
    #left eye
    #------------
    penup()
    goto(-70,130)
    pendown()
    begin_fill()
    fillcolor('#ffffff')
    circle(50,360)
    end_fill()
    penup()
    goto(-70,180)
    pendown()
    dot(30)
    penup()
    #eyebrows
    #-------------
    goto(75,270)
    pendown()
    begin_fill
    fillcolor('#3D2B1F')
    shape("circle")
    shapesize(3,.7)
    shapetransform()
    (4.0, 0.0, 0.0, 2.0)
    tilt(80)
    stamp()
    penup()

    goto(-75,270)
    pendown()
    begin_fill
    fillcolor('#3D2B1F')
    shape("circle")
    shapesize(3,.7)
    shapetransform()
    (4.0, 0.0, 0.0, 2.0)
    tilt(200)
    stamp()
    hideturtle()
    penup()
    #mouth
    #-------------
    goto(0,55)
    showturtle()
    shape("square")
    shapetransform(3, 0, 0, .7)
    tilt(90)
    #------------
    
    continue_x = False
done()