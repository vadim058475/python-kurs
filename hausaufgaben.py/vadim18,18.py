import turtle

player = turtle.Turtle()
window = turtle.Screen()

player.pensize(10)
player.pencolor('blue')
window.bgcolor('black')


def draw():
    player.clear()
    for _ in range(4):
        player.forward(100)
        player.right(90)
    turtle.ontimer(draw, 500) 

draw()  
window.mainloop()  