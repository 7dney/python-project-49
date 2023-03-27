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


def calc(): # noqa C901
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nWhat is the result of the expression?")
    counter = 0
    while counter < 3:
        mark = sign()
        numb1 = random.randint(1, 30)
        numb2 = random.randint(1, 30)
        express = f'{numb1} {mark} {numb2}'
        print(f"Question: {express}")
        user_answer = prompt.string("Your answer: ")
        user_an = int(user_answer)
        if mark == '+':
            summa = numb1 + numb2
            if summa == user_an:
                print('Correct!')
            else:
                print(f''''{user_answer}' is wrong answer ;(. Correct answer'''
                      f''' was '{summa}'. Let's try again, {user_name}!''')
                return
        if mark == '-':
            subtract = numb1 - numb2
            if subtract == user_an:
                print('Correct!')
            else:
                print(
                    f''''{user_answer}' is wrong answer ;(. Correct answer'''
                    f'''was '{subtract}'. Let's try again, {user_name}!''')
                return
        if mark == '*':
            myl = numb1 * numb2
            if myl == user_an:
                print('Correct!')
            else:
                print(
                    f''''{user_answer}' is wrong answer ;(. Correct answer'''
                    f''' was '{myl}'. Let's try again, {user_name}!''')
                return
        counter = counter + 1
    print(f'Congratulations, {user_name}!')
