import turtle

i = turtle.Turtle()
turtle.screensize(canvwidth=1280, canvheight=1280,
                  bg="black")
i = turtle.Turtle()
i.pencolor("white")
i.speed(20)


for z in range(20):
    i.right(90)
    i.forward(300)
    i.left(90)
    i.forward(1)
    i.left(90)
    i.forward(300)
    i.right(90)
i.right(90)
i.forward(140)
i.left(180)

def funR():
    for x in range(20):
        i.circle(-131,90)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.circle(-131,-90)



turtle.done()