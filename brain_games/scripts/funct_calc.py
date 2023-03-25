import random
import prompt


def sign():
    numb = random.randint(1, 3)
    if numb == 1:
        return '+'
    elif numb == 2:
        return '-'
    else:
        return '*'


def calc():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nWhat is the result of the expression?")
    counter = 0
    while counter < 3:
        mark = sign()
        namber1 = random.randint(1, 30)
        namber2 = random.randint(1, 30)
        express = f'{namber1} {mark} {namber2}'
        print(f"Question: {express}")
        user_answer = prompt.string("Your answer: ")
        user_an = int(user_answer)
        if mark == '+':
            summa = namber1 + namber2
            if summa == user_an:
                print('Correct!')
            else:
                print(f'''{user_answer} is wrong answer ;(. Correct answer
                 was {summa}. Let's try again, {user_name}''')
                return
        if mark == '-':
            subtract = namber1 - namber2
            if subtract == user_an:
                print('Correct!')
            else:
                print(
                    f'''{user_answer} is wrong answer ;(. Correct answer
                     was {subtract}. Let's try again, {user_name}''')
                return
        if mark == '*':
            myltip = namber1 * namber2
            if myltip == user_an:
                print('Correct!')
            else:
                print(
                    f'''{user_answer} is wrong answer ;(. Correct answer
                     was {myltip}. Let's try again, {user_name}''')
                return
        counter = counter + 1
    print(f'Congratulations {user_name}!')
