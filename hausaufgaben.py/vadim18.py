import turtle

window = turtle.Screen()
player = turtle.Turtle()

player.speed(0)

player.penup()
player.right(90)
player.forward(200)
player.right(90)
player.forward(150)
player.left(180)
player.pendown()



player.pensize(10)
player.pencolor('green')
for _ in range(4):
    player.forward(300)
    player.left(90)


player.penup()
player.left(90)
player.forward(310)
player.right(90)
player.pendown()


player.pensize(10)
player.pencolor('green')
for _ in range(3):
    player.forward(300)
    player.left(120)


player.penup()
player.forward(175)
player.left(90)
player.forward(120)
player.pendown()


player.pensize(3)
player.circle(30)



player.penup()
player.left(180)
player.forward(425)
player.left(180)
player.pendown()


player.forward(100)
player.left(90)
player.forward(60)
player.left(90)
player.forward(100)

player.penup()
player.left(180)
player.forward(170)
player.right(90)
player.forward(80)
player.pendown()


player.pencolor('green')
for _ in range(4):
    player.forward(80)
    player.left(90)

player.penup()
player.forward(40)
player.left(90)
player.pendown()

player.forward(80)


player.penup()
player.left(90)
player.forward(40)
player.left(90)
player.forward(40)
player.left(90)
player.pendown()

player.forward(80)



player.penup()
player.forward(100)
player.right(90)
player.forward(200)
player.left(90)
player.pendown()



window.mainloop()