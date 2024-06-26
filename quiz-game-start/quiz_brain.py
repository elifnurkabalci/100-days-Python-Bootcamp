class QuizBrain:
  
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.true = 0

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("You got it right!")
      self.true +=1
    else:
      print("That is wrong.")

    print(f"Your current score is: {self.true}/{self.question_number}")
    
  def next_quesiton(self):
    current_question = self.question_list[self.question_number]
    self.question_number +=1
    user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False)? : ")
    self.check_answer(user_answer, current_question.answer)
    