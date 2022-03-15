from os import remove
import turtle
import pandas
from state import State

#50 States game

screen = turtle.Screen()
screen.title("U.S States Game")
image = "day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


correct_guesses = 0
out_of_total = 0
guessed_states = []

while len(guessed_states) < 50:
    state_data = pandas.read_csv("day25/50_states.csv")

    list_of_states = state_data.state.to_list()
    list_of_xs = state_data.x.to_list()
    list_of_ys = state_data.y.to_list()

    out_of_total = len(list_of_states)

    answer_state = screen.textinput(f"Guess the State {correct_guesses}/{out_of_total}", "What's another state?").title()
    #receive the name of the guessed state
    #check if its a state in the 50_states csv

    answer_state_row = state_data[state_data.state == answer_state]

    missing_states = []

    if answer_state == "Exit":
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
        
        states_to_learn_frame = pandas.DataFrame(missing_states)
        states_to_learn_frame.to_csv("day25/states_to_learn.csv")
        break

    if answer_state in list_of_states:
        print("yup", answer_state)
        state_index = list_of_states.index(answer_state)
        correct_guesses += 1
        guessed_states.append(answer_state)
        # new_state = State(list_of_states[state_index], (list_of_xs[state_index], list_of_ys[state_index]))
        new_state = State(answer_state, (int(answer_state_row.x), int(answer_state_row.y)))

        #remove them from the list
        removed_state = list_of_states.pop(state_index)
        removed_x = list_of_xs.pop(state_index)
        removed_y = list_of_ys.pop(state_index)
        print("removed", removed_state)
        
    else:
        print("nope", answer_state)

states_to_learn = {"states" : [list_of_states]}
