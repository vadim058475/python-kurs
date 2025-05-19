import turtle
import time

# Налаштування екрану
window = turtle.Screen()
window.bgcolor("black")
window.title("Анімація світлофора")

# Створюємо черепашку
square = turtle.Turtle()
square.shape("square")
square.penup()
square.speed(0)
square.shapesize(3, 3)  # робимо квадрат більшим

# Список кольорів для імітації світлофора
colors = ["red", "green"]

# Малюємо 5 квадратів у ряд
squares = []
start_x = -100
for i in range(5):
    sq = square.clone()
    sq.goto(start_x + i * 50, 0)
    squares.append(sq)

# Анімація зміни кольорів
while True:
    for color in colors:
        for sq in squares:
            sq.color(color)
        time.sleep(1)  # затримка між змінами кольору