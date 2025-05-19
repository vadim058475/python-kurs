import turtle

# Налаштування вікна
screen = turtle.Screen()
screen.bgcolor("white")

# Функція для підпису фігури
def label(t, text, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text, align="center", font=("Arial", 14, "normal"))

# Створення "олівця"
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(3)

# Малюємо квадрат
pen.penup()
pen.goto(-200, 0)
pen.pendown()
for _ in range(4):
    pen.forward(100)
    pen.right(90)
label(pen, "Квадрат", -150, -20)

# Малюємо коло
pen.penup()
pen.goto(0, -50)  # Центр кола
pen.pendown()
pen.circle(50)
label(pen, "Коло", 0, -110)

# Малюємо трикутник
pen.penup()
pen.goto(150, 0)
pen.pendown()
for _ in range(3):
    pen.forward(100)
    pen.left(120)
label(pen, "Трикутник", 200, -20)

# Завершення
pen.hideturtle()
screen.mainloop()