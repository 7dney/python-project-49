import random
import prompt
from math import gcd


def gcd_f():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nFind the greatest"
          f" common divisor of given numbers.")
    counter = 0
    while counter < 3:
        a = random.randint(25, 100)
        b = random.randint(1, 25)
        c = gcd(a, b)
        print(f"Question: {a} {b}")
        user_answer = prompt.string("Your answer: ")
        user_an = int(user_answer)
        if user_an == c:
            print('Correct!')
        else:
            print(f''''{user_answer}' is wrong answer ;(. Correct'''
                  f"answer was '{c}'. Let's try again, {user_name}")
            return
        counter = counter + 1
    print(f'Congratulations, {user_name}!')
