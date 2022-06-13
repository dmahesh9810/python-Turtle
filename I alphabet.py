import turtle
turtle.screensize(canvwidth=1280, canvheight=1280,
                  bg="white")
i = turtle.Turtle()
i.speed(40)
a = v = 20
s = g = 200


def iFunction():
        i.backward(s)
        i.right(90)
        i.forward(1)
        i.left(90)
        i.forward(s)
        i.right(90)
        i.forward(1)
        i.left(90)

for b in range(a):
    iFunction()
    if b >= a - 1:
        i.backward(s/2)
        a = (s // 2)
        s = g // 2 - v * 2
        i.forward(s/2)
        for q in range(a):
            iFunction()
            if q >= a -1:
                i.backward(s/2)
                a = v
                s = g
                i.forward(s/2)
                for d in range(a):
                    iFunction() 
        
                
i.hideturtle()    
turtle.done()