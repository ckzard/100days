from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import quizInterface



question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))


new_quiz_brain = QuizBrain(question_bank)
new_ui = quizInterface(new_quiz_brain)

# new_quiz.next_question()