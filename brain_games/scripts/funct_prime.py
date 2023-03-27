import random
import prompt
import math


def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True


def prime():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f'''Hello, {user_name}!\nAnswer"yes" if given number is prime.'''
          f''' Otherwise answer "no".''')
    n = 0
    while n < 3:
        a = random.randint(1, 100)
        print(f'Queston: {a}')
        user_answer = prompt.string("Your answer: ")
        user_an = is_prime(a) and 'yes' or 'no'
        if user_answer == user_an:
            print('Correct!')
        else:
            print(f'''{user_answer} is wrong answer ;(. Correct'''
                  f" answer was {user_an}. Let's try again, {user_name}")
            return
        n = n + 1
    print(f'Congratulations {user_name}!')
