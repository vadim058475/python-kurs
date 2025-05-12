import turtle

window = turtle.Screen()
window.setup(width=500, height=500)
window.bgcolor("dark red")
window.title("My Python Game")

player = turtle.Turtle()
player.color("red")
player.shape("turtle")

player_text = int(input("write number: "))

if player_text > 0:
    player.forward(player_text)
elif player_text < 0:
    player.backward(abs(-player_text))
else:
    print("turtle no move")

window.mainloop()













