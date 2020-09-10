from turtle import *
Pen()
#bgcolor("green")
bgpic("pic.PNG")
color('red')
forward(90)
print(fillcolor())
left(45)
color('yellow')
forward(90)
print(fillcolor())
lt(45)
color('blue')
fd(90)
print(fillcolor())
goto(0,0)
color('black')
fd(90)
print(fillcolor())
goto(50,50)
circle(50)
goto(70,70)
dot(20,'red')

goto(120,120)
backward(90)

for i in range(4):
    fd(50)
    lt(80)
for i in range(4):
    undo()# delete draw last
textinput("NIM", "Name of first player:")#receive input from user
done()# this stop screen turtle graphics