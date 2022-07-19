import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("India States Game")
image = "blank_states_india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("28_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 28:
    answer_state = (screen.textinput(title=f"{len(guess_states)}/28 states correct", prompt="What's another state's "
                                                                                            "name?")).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(float(data[data["state"] == answer_state].x), float(data[data["state"] == answer_state].y))
        t.write(answer_state)
        guess_states.append(answer_state)



