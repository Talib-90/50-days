import turtle
import pandas as pd

image = "Day_18/blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Quiz")
screen.addshape(image)
turtle.shape(image)

# Get X and Y coordinates:
# def get_XY_coordinates(x, y):
#     print(x, y)

# screen.onscreenclick(get_XY_coordinates)

state_data = pd.read_csv("Day_18/50_states.csv")
state_list = state_data.state.tolist()
states = []

while len(states) < 50:
    answer_state = screen.textinput(title=f"{len(states)}/50 State Guess", prompt="What's another state name?").title()
    if answer_state in state_list:
        states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = state_data[state_data.state == answer_state]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)
    elif answer_state == "Exit":
        # missing_states = []
        # for state in state_list:
        #     if state not in states:
        #         missing_states.append(state)
        missing_states = [state for state in state_list if state not in states]
        missing_dataFrame = pd.DataFrame(missing_states)
        missing_dataFrame.to_csv("Day_18/Not guess states.csv")
        break
