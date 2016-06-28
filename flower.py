import turtle

def flower():
    #create screen
    window = turtle.Screen()
    window.bgcolor("green")
    #Create Petals using triangle
    flwr = turtle.Turtle()
    flwr.speed(0.1)
    n=0
    def leaf():
        flwr.circle(50)
    for n in range(1,100):
        leaf()
        flwr.right(n)
        flwr.fillcolor("red")
        n=n+1
    flwr.backward(300)

    
    window.exitonclick()
    
flower()
        
    
