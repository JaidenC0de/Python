from turtle import *
#First color is pencolor second is fillcolor.
color('black', 'yellow')
while True:
    penup()
    goto(90,200)
    pendown()
    circle(50,360)
    penup()
    home()
    penup()
    goto(-90,200)
    pendown()
    circle(50,360)
    penup()
    home()
    begin_fill()
    circle(200,360)
    end_fill()
#   forward(200)
#    setx(90)
#    sety(200)
#    left(90)
#    right()
#    home()
#    stamp()
    if abs(pos()) < 1:
        break
done()