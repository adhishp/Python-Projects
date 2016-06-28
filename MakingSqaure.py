import turtle

def shape():
        screen = turtle.Screen()
        screen.bgcolor("black")
        i=0
        sqr = turtle.Turtle()
        def square():
                sqr.color("red")
                sqr.speed(0.01)
        #Create Square
                n=1
                while n<5:
                    sqr.forward(200)
                    sqr.right(90)
                    n=n+1
        #Create Circle
        
        while i<366:
                sqr.right(i)
                square()
                i=i+1
        #Create Triangle
        #move.color("blue")
        #move.backward(200)
        #move.right(60)
        #move.forward(200)
        #move.left(120)
        #move.forward(200)
        
        screen.exitonclick()
shape()
