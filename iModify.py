import turtle
turtle.screensize(canvwidth=1280, canvheight=1280,
                  bg="black")
i = turtle.Turtle()
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
i.hideturtle()    
turtle.done()