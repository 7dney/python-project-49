import random
from math import gcd


CONDITION = 'Find the greatest common divisor of given numbers.'


def get_question_and_right_answer():
    a = random.randint(25, 100)
    b = random.randint(1, 25)
    c = gcd(a, b)
    question = f'{a} {b}'
    return question, str(c)
