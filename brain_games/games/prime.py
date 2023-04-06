import random
import math


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_right_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True
