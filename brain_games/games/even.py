import random


CONDITION = '''Answer "yes" if the number is even, otherwise answer "no".'''


def funct_game():
    namber = random.randint(1, 100)
    if namber % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (namber, answer)
