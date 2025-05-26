# import turtle as t 



# t.speed(0)
# t.bgcolor('black')
# t.pencolor('orange')
# def squere(x, y):
#     for j in range(4):
#         t.forward(x)
#         t.right(y)

# for i in  range(80):
#     squere(170, 90)
#     t.right(5)
#     t.circle(50)
#     t.right(50)
#     t.hideturtle()

# t.done()    

import turtle
import time
import random

# Налаштування екрану
win = turtle.Screen()
win.title("Гра Змійка")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Вимкнути автоматичне оновлення екрана

# Голова змійки
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Їжа
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Список для тіла змійки
segments = []

# Рахунок
score = 0

# Функції для управління напрямком
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

# Рух голови
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Прив’язка клавіш
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Основний цикл гри
while True:
    win.update()

    # Перевірка зіткнення зі стінами
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0

    # Перевірка зіткнення з їжею
    if head.distance(food) < 20:
        # Перемістити їжу у випадкове місце
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Додати новий сегмент тіла
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        print("Рахунок:", score)

    # Переміщення сегментів тіла
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Перевірка зіткнення з тілом
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            print("Гру закінчено!")

    time.sleep(0.1)