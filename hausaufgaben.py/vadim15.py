import turtle

# Запит у користувача
first_name = input("Введіть ваше ім'я: ")
last_name = input("Введіть ваше прізвище: ")
color = input("Введіть ваш улюблений колір (англійською): ")

# Налаштування Turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.color(color)
pen.penup()
pen.goto(0,0)
pen.write(f"{first_name} {last_name}", align="center", font=("Arial black", 50, "bold"))

screen.mainloop()