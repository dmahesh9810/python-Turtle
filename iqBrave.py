import turtle
turtle.screensize(canvwidth=2000, canvheight=2000,
                  bg="black")
i = turtle.Turtle()
i.penup()
i.speed(5)
i.backward(600)
i.left(90)
i.forward(100)
i.right(90)
i.pendown()
i.pencolor("white")
i.hideturtle() 
i.left(180)
i.penup()
i.hideturtle()    
i.circle(-30,90)
i.pendown()
i.showturtle()
i.speed(20)
s = 10
def ifun1():
    for x in range(s):
        i.circle(-30,-90)
        i.backward(180)
        i.circle(30,-90)
        i.left(90)
        i.forward(1)
        i.right(90)
        i.circle(29,90)
        i.forward(180)
        i.circle(-30,90)

def ifun2():
    for q in range(s*s):
        i.left(90)
        i.forward(1)
        i.left(90)
        i.forward(20)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.backward(20)
        i.left(180)
        if q >= s*10-1:
            i.forward(90)
            i.circle(-30,90)
            ifun1()

ifun1()
i.circle(-30,-90)
i.backward(90)
ifun2()
i.right(90)
i.penup()
i.forward(410)
i.left(90)
i.forward(170)
i.pendown()
i.right(90)

def ss():
    for s in range(10):
        i.left(135)
        i.circle(100,270)
        i.left(90)
        i.forward(1)
        i.right(90)
        i.circle(100,-270)
        i.right(135)
def dd():
    for d in range(10):
        i.backward(300)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.forward(300)

def aa():
    for ff in range(10):
        i.forward(60)
        i.left(90)
        i.forward(1)
        i.right(90)
        i.backward(60)

def funR():
    for x in range(15):
        i.circle(-131,90)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.circle(-131,-90)

# aa
def afun():
    for a in range(20):
        i.left(90)
        i.circle(-80,180)
        i.forward(150)
        i.circle(80,90)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.circle(81,-90)
        i.backward(150)
        i.circle(-80,-180)
        i.right(90)
        if a >= 20-1 :
            i.left(90)
            i.circle(-80,180)
            i.forward(150)
            for d in range(20):
                i.circle(-80,180)
                i.right(90)
                i.forward(1)
                i.left(90)
                i.circle(-80,180)
# aa
ss()
i.left(90)
i.forward(20)
dd()
i.backward(300)
i.right(30)
aa()
i.penup()
i.right(60)
i.right(180)
i.backward(50)
i.right(90)
i.forward(350)
i.pendown()
dd()
i.backward(300)
i.forward(30)
i.left(90)
i.forward(10)
i.right(90)
i.left(90)
ss()

i.penup()
i.backward(200)
i.right(90)
i.forward(200)
i.pendown()
i.right(90)
afun()
i.penup()
i.backward(200)
i.right(180)
i.right(90)
i.forward(90)
i.left(90)
# i.forward()
i.pendown()
# a
dd()


i.right(180)
i.forward(140)
i.left(180)
funR()

# v
i.penup()
i.right(90)
i.forward(150)
i.left(90)
i.forward(150)
i.right(90)
i.left(100)
i.pendown()
dd()

i.penup()
i.right(100)
i.forward(98)
i.pendown()
i.right(280)
dd()

# E

def efun():
    for x in range(100):
        i.circle(-110,330)
        i.circle(-109.8,-330)
        if x >= 100 - 1:
            i.circle(-109.8,150)
            i.right(90)
            for d in range(10):
                i.forward(220)
                i.right(90)
                i.forward(1)
                i.right(90)
                i.forward(220)
                i.left(90)
                i.left(90)
i.penup()
i.right(80)
i.right(90)
i.forward(200)
i.left(90)
i.forward(200)
i.right(120)
i.pendown()
# i.left(150)
# i.forward(200)

efun()
# i.hideturtle()  

turtle.done()