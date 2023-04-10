import prompt

MAX_COUNTER = 3


def welcome_user(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def game_engine(game):
    user_name = welcome_user(game)
    print(game.CONDITION)
    count = 0
    while MAX_COUNTER > count:
        question, right_answer = game.get_question_and_right_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        answer = user_answer
        if answer != right_answer:
            print(f"'{answer}' is wrong answer ;(.",
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
        count += 1
    print(f'Congratulations, {user_name}!')
