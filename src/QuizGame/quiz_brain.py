class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {question.text} (True/False) ")
        self.check_answer(user_answer, question.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def increment_score(self):
        self.score += 1

    def check_answer(self, user_answer, correct_answer):
        user_answer = user_answer.lower()
        correct_answer = correct_answer.lower()
        if user_answer == correct_answer:
            print("You got it right!")
            self.increment_score()
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer.capitalize()}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
    
    def get_score(self):
        return self.score
    
    def get_question_number(self):
        return self.question_number
