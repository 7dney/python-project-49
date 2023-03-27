import random
import prompt


yes = 'yes'
no = 'no'


def even():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f'''Hello, {user_name}!\nAnswer "yes" if the number is even, '''
          f'''otherwise answer "no".''')

    counter = 0
    while counter < 3:
        namber = random.randint(1, 100)
        print(f"Question: {namber}")
        user_answer = prompt.string("Your answer: ")
        if namber % 2 == 0:
            if user_answer == yes:
                print('Correct!')
            else:
                print(f''''yes' is wrong answer ;(. Correct answer was 'no'.'''
                      f'''Let's try again, {user_name}''')
                return
        elif namber % 2 != 0:
            if user_answer == no:
                print('Correct!')
            else:
                print(f''''yes' is wrong answer ;(. Correct answer was 'no'.'''
                      f'''Let's try again, {user_name}''')
                return
        else:
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.'''
                  f'''Let's try again, {user_name}''')
            return
        counter = counter + 1
    print(f'Congratulations {user_name}!')
