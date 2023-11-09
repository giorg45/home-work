from turtle import *
shape("turtle")
#square
speed(50)
width(5)
color("dark blue")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
end_fill()

#roof
penup()
goto(200,200)
pendown()
color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#windows
penup()
goto(130,110)
pendown()
color("gold")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(70,110)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50) 
right(90)
forward(50)
end_fill()


#grass
penup()
goto(-380,-200)
pendown()
color("green")
begin_fill()
left(90)
forward(750)
right(90)
forward(110)
right(90)
forward(750)
right(90)
forward(110)
end_fill()

#pool
penup()
goto(-370,-100)
pendown()
color("blue")
begin_fill()
right(90)
forward(200)
left(60)
forward(100)
left(120)
forward(200)
left(60)
forward(100)
end_fill()   

penup()
goto(-390,-120)
pendown()
color("black")
left(120)
forward(250)
left(60)
forward(150)
left(120)
forward(270)
left(60)
forward(150)




exitonclick()






