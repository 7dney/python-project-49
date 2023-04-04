import prompt


def welcome_user(CONDITION):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name, CONDITION


def go_answer(question):
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ")
    return user_answer


def game_engine(game):

    user_name, CONDITION = welcome_user(game.CONDITION)
    print(CONDITION)
    count = 0

    while count < 3:
        question, right_answer = game.funct_game()
        answer = go_answer(question)
        if answer != right_answer:
            print(f''''{answer}' is wrong answer ;(.''',
                  f'''Correct answer was '{right_answer}'.''')
            print(f'''Let's try again, {user_name}!''')
            return
        print('Correct!')
        count += 1
    print(f'Congratulations, {user_name}!')
