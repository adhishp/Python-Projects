import turtle

def myinitials():
    window = turtle.Screen()
    window.bgcolor("blue")
    #drawing A
    a = turtle.Turtle()
    a.left(75)
    a.forward(200)
    a.right(150)
    a.forward(200)
    a.backward(100)
    a.right(105)
    a.forward(55)
    #drwaing P
    p = turtle.Turtle()
    p.color("blue")
    p.forward(150)
    p.color("black")
    p.left(90)
    p.forward(200)
    p.right(90)
    p.circle(-60,180)
    
    #exit fucntion
    window.exitonclick()

myinitials()
