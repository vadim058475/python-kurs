import turtle


screen = turtle.Screen()
screen.title("Зміна фону залежно від часу доби")

hour = int(input("Введіть годину (0–23): "))


if 5 <= hour <= 11:
    screen.bgcolor("lightblue")  
elif 12 <= hour <= 16:
    screen.bgcolor("skyblue")    
elif 17 <= hour <= 20:
    screen.bgcolor("orange")     
else:
    screen.bgcolor("midnightblue")  


turtle.done()