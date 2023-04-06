import random


CONDITION = 'What is the result of the expression?'


def sign():
    numb = random.choice('+-*')
    return numb


def get_question_and_right_answer():
    mark = sign()
    numb1 = random.randint(1, 30)
    numb2 = random.randint(1, 30)
    question = f'{numb1} {mark} {numb2}'
    if mark == '+':
        us_answer = numb1 + numb2
        return question, str(us_answer)
    if mark == '-':
        us_answer = numb1 - numb2
        return question, str(us_answer)
    if mark == '*':
        us_answer = numb1 * numb2
        return question, str(us_answer)
