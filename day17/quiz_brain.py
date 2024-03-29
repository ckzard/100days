#asking questions
#checking if the answer was correct
#checking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
       # return a boolean if the question list still has questions
        return self.question_number < len(self.question_list)  
    
    def next_question(self):

        keep_going = self.still_has_questions()

        while keep_going:
            
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            show_question = input(f"Q.{self.question_number}: {current_question.text} Please enter True or False: \n")

            if show_question == current_question.answer:
                print("You got it right!")
                self.score += 1
            else:
                print("NAh you wrong G!")
            
            keep_going = self.still_has_questions()
        
        print("\n")
        print("Thats the end of the quiz here are your results:")
        print(f"{self.score} / {len(self.question_list)}")

        
    