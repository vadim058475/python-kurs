import turtle

# Створення вікна
screen = turtle.Screen()
screen.title("Зміна фону залежно від часу доби")

# Ввід користувача
hour = int(input("Введіть годину (0–23): "))

# Зміна кольору фону залежно від часу
if 5 <= hour <= 11:
    screen.bgcolor("lightblue")  # Ранок
elif 12 <= hour <= 16:
    screen.bgcolor("skyblue")    # День
elif 17 <= hour <= 20:
    screen.bgcolor("orange")     # Вечір
else:
    screen.bgcolor("midnightblue")  # Ніч

# Затримка закриття вікна
turtle.done()