import turtle


color1 = input('Введіть перший улюблений колір: ')
color2 = input('Введіть другий улюблений колір: ')
color3 = input('Введіть третій улюблений колір: ')


screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


pen.color(color1)
pen.goto(0, 40)
pen.write("Hello, World!", align="left", font=("Arial", 24, "bold"))


pen.color(color2)
pen.goto(0, 0)
pen.write("Hello, World!", align="left", font=("Courier", 24, "italic"))


pen.color(color3)
pen.goto(0, -40)
pen.write("Hello, World!", align="left", font=("Times New Roman", 24, "normal"))

screen.mainloop()