import turtle

i = turtle.Turtle()
turtle.screensize(canvwidth=1280, canvheight=1280,
                  bg="black")
i = turtle.Turtle()
i.pencolor("white")
i.speed(20)

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
        i.backward(350)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.forward(350)

def aa():
    for ff in range(10):
        i.forward(60)
        i.left(90)
        i.forward(1)
        i.right(90)
        i.backward(60)

ss()
i.left(90)
i.forward(20)
dd()
i.backward(350)
i.right(30)
aa()
turtle.done()