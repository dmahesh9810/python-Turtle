import turtle

i = turtle.Turtle()
turtle.screensize(canvwidth=1280, canvheight=1280,
                  bg="black")
i = turtle.Turtle()
i.pencolor("white")
i.speed(20)

i.right(120)

def efun():
    for x in range(100):
        i.circle(-100,330)
        i.circle(-99.8,-330)
        if x >= 100 - 1:
            i.circle(-99.8,150)
            i.right(90)
            for d in range(10):
                i.forward(200)
                i.right(90)
                i.forward(1)
                i.right(90)
                i.forward(200)
                i.left(90)
                i.left(90)




turtle.done()