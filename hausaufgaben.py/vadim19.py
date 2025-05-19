import turtle

window = turtle.Screen()
player = turtle.Turtle()

player.pencolor('blue')
player.pensize(10)
player.shape('turtle')
player.shapesize(1)



x = int(input('Введи число x: '))  
y = int(input('Введи число y: '))  

player.goto(x,y)































window.mainloop()