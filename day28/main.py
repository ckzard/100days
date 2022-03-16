
from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    # stop timer
    window.after_cancel(timer)
    #reset checks
    check_mark.config(text="")
    #reset the text to Timer
    title_label.config(text="Timer", fg=GREEN)
    # set timer back to 00:00 or 25:00
    canvas_5.itemconfig(timer_text, text="00:00")
    #reset reps
    global reps
    reps = 0    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1
    

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down (long_break_sec)
        #long break
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        #short break
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        #working
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #format count as 00:00
    global reps
    
    minutes_remaining = int(math.floor(count / 60))
    seconds_remaining = count % 60
    check_text="✔" 
    # if minutes_remaining < 1:
    #     minutes_remaining = "00"

    if seconds_remaining == 0:
        seconds_remaining = "00"
    elif seconds_remaining < 10:
        seconds_remaining = "0" + str(seconds_remaining)

    canvas_5.itemconfig(timer_text, text=f"{minutes_remaining}:{seconds_remaining}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks = ""
            for num in range(math.floor(reps/2)):
                marks += check_text
            check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# configuring the window
window = Tk()
window.title("Pomodoro")
window.config(padx=0, pady=0, bg=YELLOW)

canvas_1 = Canvas(width=100, height=100, bg=YELLOW, highlightthickness=0)
canvas_1.grid(column=0, row=0)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas_3 = Canvas(width=100, height=100, bg=YELLOW, highlightthickness=0)
canvas_3.grid(column=2, row=0)

canvas_4 = Canvas(width=100, height=224, bg=YELLOW, highlightthickness=0)
canvas_4.grid(column=0, row=1)

#adding an image onto the canvas
canvas_5 = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28/tomato.png")
canvas_5.create_image(100, 112, image=tomato_img)
timer_text = canvas_5.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas_5.grid(column=1, row=1)

canvas_6 = Canvas(width=100, height=224, bg=YELLOW, highlightthickness=0)
canvas_6.grid(column=2, row=1)


canvas_7 = Canvas(width=100, height=10, bg=YELLOW, highlightthickness=0)
canvas_7.grid(column=0, row=2)
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

canvas_8 = Canvas(width=200, height=20, bg=YELLOW, highlightthickness=0)
canvas_8.grid(column=1, row=2)

canvas_9 = Canvas(width=100, height=20, bg=YELLOW, highlightthickness=0)
canvas_9.grid(column=2, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

canvas_10 = Canvas(width=100, height=20, bg=YELLOW, highlightthickness=0)
canvas_10.grid(column=0, row=3)

canvas_11 = Canvas(width=200, height=20, bg=YELLOW, highlightthickness=0)
canvas_11.grid(column=1, row=3)
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas_12 = Canvas(width=100, height=20, bg=YELLOW, highlightthickness=0)
canvas_12.grid(column=2, row=3)

canvas_13 = Canvas(width=100, height=30, bg=YELLOW, highlightthickness=0)
canvas_13.grid(column=0, row=4)

canvas_14 = Canvas(width=200, height=30, bg=YELLOW, highlightthickness=0)
canvas_14.grid(column=1, row=4)

canvas_15 = Canvas(width=100, height=30, bg=YELLOW, highlightthickness=0)
canvas_15.grid(column=2, row=4)

window.mainloop()