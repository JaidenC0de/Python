from turtle import *
color('black', 'yellow')
begin_fill()
while True:
    circle(200,360)
    penup()
    if abs(pos()) < 1:
        break
end_fill()
done()