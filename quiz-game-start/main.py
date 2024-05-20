from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for a in question_data:
    text = a["text"]
    answer = a["answer"]
    question_bank.append(Question(text, answer))

#print(question_bank[0].text)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_quesiton()

print(f"You've completed the quiz")
print(f"Your final score is {quiz.true}/{quiz.question_number}.")
