import turtle as tom
import random

tom.clearscreen() #clear the screen

tom.colormode(225)
tom.bgcolor("Dark Blue")#BackGround color

tom.shape("turtle")#make tom a turtle and not an arrow
tom.shapesize(2, 2, 4) # Make tom bigger
col = ['red', 'purple', 'yellow', 'orange', 'green', 'blue', 'pink'] 


def drawhearts():
    tom.setheading(0)#point east
    tom.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    #set Tom's X and Y
    tom.fillcolor(col[random.randint(0, 6)])#set Tom's color
    tom.begin_fill()#start filling
    tom.goto(x, y)
    tom.pendown()
    tom.left(125)
    tom.forward(205 * size)
    tom.right(35)
    curve()
    tom.left(180)
    curve()
    tom.right(35)
    tom.forward(195 * size)
    tom.end_fill()#end filling
    
def curve():
    for i in range(45):
        tom.right(4)
        tom.forward(4 * size)

def drawstars():
    points = (random.randint(2, 3) * 2) + 1
    tom.setheading(0)#point east
    tom.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    #set Tom's X and Y
    tom.fillcolor(col[random.randint(0, 6)])#set Tom's color
    tom.begin_fill()#start filling
    tom.goto(x, y)
    tom.pendown()
    tom.begin_fill()
    for i in range (5):
        tom.right(144)
        tom.forward(100 * size)
    tom.end_fill()

def rewrite():
    tom.penup()
    tom.goto(0, 0)
    tom.pendown()
    tom.write("Happy Birthday ____!", align="Center", font=("Arial", 40, "normal"))
#insert name here...        /|\
while True:
    rewrite()
    size = random.randint(5, 10)/20
    tom.width(5)
    drawhearts()
    size = random.randint(5, 10)/10
    tom.width(10 * size)
    drawstars()
