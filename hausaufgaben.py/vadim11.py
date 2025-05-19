import turtle

window = turtle.Screen()
player = turtle.Turtle()


player.pensize(10)
player.pencolor('green')
for _ in range(4):
    player.forward(100)
    player.left(90)

player.penup()
player.left(180)
player.forward(200)
player.pendown()



player.pensize(10)
player.pencolor('blue')
for _ in range(360):
    player.forward(2)
    player.left(1)


player.penup()
player.right(90)
player.forward(150)
player.right(90)
player.forward(50)
player.left(90)
player.forward(50)
player.pendown()



player.speed(5)
player.pensize(10)
player.pencolor('red')
for _ in range(6):
    player.forward(100)
    player.left(60)




window.mainloop()