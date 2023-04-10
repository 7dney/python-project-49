import random


CONDITION = 'What is the result of the expression?'


def get_question_and_right_answer():
    operation = ['+', '-', '*']
    operation = random.choice(operation)
    number1 = random.randint(1, 30)
    number2 = random.randint(1, 30)
    question = f'{number1} {operation} {number2}'
    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    elif operation == '*':
        correct_answer = str(number1 * number2)
    return question, correct_answer
