from cgitb import text
from re import L
from sqlite3 import Row
from textwrap import fill
from tkinter import *
from turtle import bgcolor, color
from urllib import response
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class quizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain
        self.number_of_questions = len(self.quiz.question_list)
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(height=600, width=400, bg=THEME_COLOR)

        self.score_text = Label(bg=THEME_COLOR, font=("Arial", 10, "bold"), fg="white")
        self.score_text.grid(row=0, column=1, padx=20, pady=20)
        self.score_text.config(text=f"Score: {self.quiz.score}")

        self.canvas_1 = Canvas(bg="white")
        self.canvas_1.grid(column=0, row=1, columnspan=2, padx=25, pady=25)
        self.question_text = self.canvas_1.create_text(200, 125, width=380, text="question goes here", font=("Arial", 15, "italic"), fill="black")

        self.check_image = PhotoImage(file="day34/images/checkmarkquiz.png")
        self.check_button = Button(image=self.check_image, command=self.true_click)
        self.check_button.grid(column=0, row=2, pady=25)

        x_image = PhotoImage(file="day34/images/xmarkquiz.png")
        self.x_button = Button(image=x_image, command=self.false_click)
        self.x_button.grid(column=1, row=2, pady=25)
        
        self.get_next_question()

        self.window.mainloop()
    
    def update_score(self):
        self.score_text.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas_1.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas_1.itemconfig(self.question_text, text=q_text)

    def give_feedback(self, response):

        if response == True:
            self.canvas_1.config(bg="green")
        else:
            self.canvas_1.config(bg="red")

        keep_going = self.quiz.still_has_questions()

        if keep_going:
            self.window.after(1000, self.get_next_question)
        else:
            print("no more questions left")
            self.canvas_1.itemconfig(self.question_text, text=f"End of Quiz \n You scored {self.quiz.score}/{self.number_of_questions}", bg="white")

    def true_click(self):
        self.answer = "True"
        self.response = self.quiz.check_answer(self.answer)
        self.give_feedback(self.response)
        self.update_score()

    def false_click(self):
        self.answer = "False"
        self.response = self.quiz.check_answer(self.answer)
        self.give_feedback(self.response)
        self.update_score()
        
