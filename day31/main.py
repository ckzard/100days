from cgitb import text
from email.mime import image
from textwrap import fill
from tkinter import *
from numpy import flip
import pandas
from random import *
import time

# ======================================================================================
current_card = {}
to_lear = {}

try:
    data = pandas.read_csv("day31/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day31/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas_1.itemconfig(card_title, text="French", fill="black")
    canvas_1.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas_1.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas_1.itemconfig(card_title, text="English")
    canvas_1.itemconfig(card_word, text=current_card["English"])
    canvas_1.itemconfig(card_image, image=card_back)
    canvas_1.itemconfig(card_title, fill="white")
    canvas_1.itemconfig(card_word, fill="white")

def know_word():
    if len(to_learn) == 1:
        data = pandas.read_csv("day31/french_words.csv")
        new_to_learn = data.to_dict(orient="records")
        new_df = pandas.DataFrame(new_to_learn)
        new_df.to_csv("day31/words_to_learn.csv", index=False)
        canvas_1.itemconfig(card_title, text="Congratulations")
        canvas_1.itemconfig(card_word, text="The End")
    else:
        to_learn.remove(current_card)
        print(len(to_learn))
        new_df = pandas.DataFrame(to_learn)
        new_df.to_csv("day31/words_to_learn.csv", index=False)
        next_card()   
# ======================================================================================
GREEN = "#9bdeac"
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=GREEN)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="day31/card_front.png")
card_back = PhotoImage(file="day31/card_back.png")

canvas_1 = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card_image = canvas_1.create_image(400, 263, image=card_front)
card_title = canvas_1.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas_1.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas_1.grid(column=1, row=1, columnspan=2)

check_mark = PhotoImage(file="day31/checkmark.png")
x_mark = PhotoImage(file="day31/xmark.png")

button_check = Button(image=check_mark, highlightthickness=0, command=know_word)
button_x = Button(image=x_mark, highlightthickness=0, command=next_card)

button_check.grid(column=1, row=2)
button_x.grid(column=2, row=2)

next_card()


window.mainloop()