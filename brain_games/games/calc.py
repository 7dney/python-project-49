import random


CONDITION = 'What is the result of the expression?'


def sign():
    numb = random.randint(1, 3)
    if numb == 1:
        return '+'
    elif numb == 2:
        return '-'
    else:
        return '*'


def funct_game():
    mark = sign()
    numb1 = random.randint(1, 30)
    numb2 = random.randint(1, 30)
    namber = f'{numb1} {mark} {numb2}'
    if mark == '+':
        us_answer = numb1 + numb2
        return namber, str(us_answer)
    if mark == '-':
        us_answer = numb1 - numb2
        return namber, str(us_answer)
    if mark == '*':
        us_answer = numb1 * numb2
        return namber, str(us_answer)
