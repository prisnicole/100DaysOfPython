import random


class QuizModel:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        """
        takes user answer and checks against the answer for that question
        """
        if user_answer == self.answer:
            return True
        else:
            return False


def generate_question():
    from quiz_questions import question_bank
    question, answer = random.choice(list(question_bank.items()))

    return QuizModel(question, answer)
