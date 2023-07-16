from classes.question_model import Question
from classes.quiz_brain import QuizBrain
from data.questions import question_data

question_bank = []
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question = Question(text, answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.\n")
