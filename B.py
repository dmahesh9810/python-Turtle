import turtle
turtle.screensize(canvwidth=720, canvheight=1280,
                  bg="blue")
a = turtle.Turtle()

a.width(2)
a.left(90)
a.forward(400)
a.right(90)
a.forward(100)
a.circle(-100,180)
a.forward(100)
a.left(180)
a.forward(100)
a.circle(-100,180)
a.forward(100)
a.right(90)

# a.hideturtle()
turtle.done()