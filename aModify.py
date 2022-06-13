import turtle

i = turtle.Turtle()
turtle.screensize(canvwidth=1280, canvheight=1280,
                  bg="black")
i = turtle.Turtle()
i.pencolor("white")
i.speed(20)


def afun():
    for a in range(20):
        i.left(90)
        i.circle(-90,180)
        i.forward(170)
        i.circle(90,90)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.circle(91,-90)
        i.backward(170)
        i.circle(-90,-180)
        i.right(90)
        if a >= 20-1 :
            i.left(90)
            i.circle(-90,180)
            i.forward(170)
            for d in range(20):
                i.circle(-90,180)
                i.right(90)
                i.forward(1)
                i.left(90)
                i.circle(-90,180)

afun()
turtle.done()