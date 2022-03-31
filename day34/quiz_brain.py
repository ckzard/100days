#asking questions
#checking if the answer was correct
#checking if we're at the end of the quiz

import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
       # return a boolean if the question list still has questions
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):

        if answer == self.current_question.answer:
            print("You got it right!")
            self.score += 1
            return True
        else:
            print("NAh you wrong G!")
            return False

    def next_question(self):

        keep_going = self.still_has_questions()

        if keep_going:
            print('still have questins')
        else:
            return False
               

        self.current_question = self.question_list[self.question_number]
        
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)

        return f"Q.{self.question_number}: {q_text} Please enter True or False: \n"
        

        
    