from cgitb import text
from email.mime import image
from tkinter import *

GREEN = "#9bdeac"

window = Tk()

window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=GREEN)

check_mark = PhotoImage(file="day31/checkmark.png")
x_mark = PhotoImage(file="day31/xmark.png")

card_front = PhotoImage(file="day31/card_front.png")
canvas_1 = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
canvas_1.create_image(400, 256, image=card_front)
canvas_1.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
canvas_1.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
canvas_1.grid(column=1, row=1, columnspan=2)

button_check = Button(image=check_mark, highlightthickness=0)
button_x = Button(image=x_mark, highlightthickness=0)
button_check.grid(column=1, row=2)
button_x.grid(column=2, row=2)

window.mainloop()