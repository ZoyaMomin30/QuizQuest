from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for q in question_data:
    q_text = q["question"]
    q_ans = q["correct_answer"]
    new_q = Question(text=q_text, answer=q_ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("\nYou've completed the quiz! ")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")





