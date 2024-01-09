from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

# Transformando los datos tipo texto en objetos sobre los cuales puedo aplicar atributos y métodos

question_bank = []

for i in question_data:
    question = Question(i["question"],i["correct_answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
