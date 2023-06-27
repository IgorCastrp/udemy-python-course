import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turt = turtle.Turtle()

screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")

data_dict = data.to_dict()
for i in range(len(data_dict["state"])):
    print(data_dict["state"][i])
states_correct = []

game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title=f"{len(states_correct)}/50 - Guess the State", prompt="What's another "
                                                                                                "state's name?").title()
    if answer_state == "Exit":
        break
    for i in range(len(data)):
        if data_dict["state"][i] == answer_state:
            turt.goto(data_dict["x"][i], data_dict["y"][i])
            turt.ht()
            turt.write(answer_state)
            if answer_state not in states_correct:
                states_correct.append(answer_state)
                print(states_correct)
            break
    if len(states_correct) == 50:
        turtle.write("CONGRATS, YOU DONE ALL STATES", False, "center", ("Arial", 30, "normal"))
        game_is_on = False

states_to_learn = []
for i in range(len(data)):
    if data["state"][i] not in states_correct:
        states_to_learn.append(data["state"][i])

df = pd.DataFrame(states_to_learn, columns=["states"])
df.to_csv("States to Learn.csv")


