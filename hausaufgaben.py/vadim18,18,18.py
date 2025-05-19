import turtle

window = turtle.Screen()
player = turtle.Turtle()

player.speed(0)


player.pensize(10)
player.pencolor('green')
for _ in range(4):
    player.forward(150)
    player.left(90)

player.penup()
player.forward(50)
player.left(90)
player.forward(75)
player.right(90)
player.write('квадрат', align="center", font=("Arial", 18, "normal"))



player.penup()
player.left(180)
player.forward(200)
player.left(90)
player.forward(40)
player.right(180)
player.pendown()




player.speed(0)
player.pensize(10)
player.pencolor('red')
for _ in range(360):
    player.forward(1)
    player.left(1)

player.penup()
player.left(90)
player.forward(50)
player.left(180)
player.pendown()
player.write('коло', align="center", font=("Arial", 18, "normal"))


player.penup()
player.right(90)
player.forward(200)
player.left(90)
player.forward(50)
player.pendown()

player.speed(0)
player.pensize(10)
player.pencolor('green')
for _ in range(3):
    player.forward(150)
    player.left(120)



player.penup()
player.forward(75)
player.left(90)
player.forward(50)
player.right(90)
player.pendown()


player.write('трикутник', align="center", font=("Arial", 13, "normal"))










window.mainloop()