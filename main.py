from turtle import Turtle, Screen
from random import randint

race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_choose = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
y_pos = [-120, -70, -20, 30, 80, 130]

for n in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[n])
    turtle.penup()
    turtle.goto(x=-230, y=y_pos[n])
    turtles.append(turtle)

if user_choose:
    race_on = True

while race_on:
    for turtle in turtles:
        rand_distance = randint(0,10)
        turtle.fd(rand_distance)
        if turtle.xcor() > 230:
            race_on = False
            if turtle.pencolor() == user_choose:
                my_screen.textinput(title="Win", prompt=f"The {turtle.pencolor()} turtle wins!")
            else:
                my_screen.textinput(title="Lose", prompt=f"The {turtle.pencolor()} turtle wins!")
            
            
my_screen.exitonclick()