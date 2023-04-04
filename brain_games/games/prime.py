import random
import math


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def funct_game():
    namber = random.randint(1, 100)
    answer = is_prime(namber)
    return namber, answer


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            us_answer = 'no'
            return us_answer
    us_answer = 'yes'
    return us_answer
