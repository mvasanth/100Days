from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

def main():
    question_bank = []

    for q_data in question_data:
        question = Question(q_data["text"], q_data["answer"])
        question_bank.append(question)

    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print("You've completed the quiz.")
    print(f"Your final score is {quiz_brain.get_score()}/{quiz_brain.get_question_number()}.")

main()