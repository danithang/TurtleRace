import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, 90, -50, 50, -20, 20]
is_race_on = False
# creating an empty bracket to pass in turtles later
all_turtles = []


# for loop to get 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    # getting colors of turtle through turtle_index because of the range set
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # getting positions of y through the turtle_index because of the range set
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # appending new_turtle to all_turtles list
    all_turtles.append(new_turtle)

# asking if the user wants to race so the race won't start prematurely
if user_bet:
    is_race_on = True

# now starting race once user gives ok
while is_race_on:
    for turtle in all_turtles:
        # saying that the turtle with the x coordinate is greater than 230 then that turtle won, 230 is 250 - half
        # the size of the turtle 40 px
        if turtle.xcor() > 230:
            is_race_on = False
            # only getting the pencolor instead of the fillcolor of the winning turtle
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")

        # randint can be actually 0 - 10 instead of starting at 0 and not including 10
        # the distance is the amount they jump forward
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
