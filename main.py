import random

from question_model import QuizModel
from quiz_questions import question_bank


def generate_question():
    # TODO : Don't repeat questions that have been asked before
    question, answer = random.choice(list(question_bank.items()))

    return QuizModel(question, answer)


def start_quiz():
    score = 0
    while True:
        try:
            question = generate_question()
            user_answer = input(f'The capital of {question.question} is :').capitalize()
            if question.check_answer(user_answer):
                score += 1
                print(f'correct! Your score is {score}')
            else:
                print("Incorrect")
        except EOFError as e:
            print(f'Your final score is {score}')
            break


def main():
    start_quiz()


if __name__ == '__main__':
    main()
