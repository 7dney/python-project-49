from brain_games.cli import welcome_user, go_answer


def game_engine(game):
    us_name = welcome_user(game.Condition)
    count = 0

    while count < 3:
        quest, correct = game.funct_game()
        answer = go_answer(quest)
        if answer != correct:
            print(f''''{answer}' is wrong answer ;(.''',
                  f'''Correct answer was '{correct}'.''')
            print(f'''Let's try again, {us_name}!''')
            return
        print('Correct!')
        count += 1
    print(f'Congratulations, {us_name}!')
