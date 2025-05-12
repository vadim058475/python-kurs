import turtle 

window = turtle.Screen()
player = turtle.Turtle()
player.speed(5)

player.shape('turtle')



user= input('Напиши куди рухатися черепашці: вліво, вправо, вперед, назад ')


player.left(90)



if user == 'вперед':
    player.forward(100)
elif user == 'вліво':  
    player.left(90) 
    player.forward(100)
elif user == 'вправо':
    player.right(90)
    player.forward(100)
elif user == 'назад':
    player.right(180)
    player.forward(100)    


  
window.mainloop()