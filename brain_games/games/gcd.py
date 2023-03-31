import random
from math import gcd


Condition = 'Find the greatest common divisor of given numbers.'


def funct_game():
    a = random.randint(25, 100)
    b = random.randint(1, 25)
    c = gcd(a, b)
    namber = f'{a} {b}'
    return namber, str(c)
