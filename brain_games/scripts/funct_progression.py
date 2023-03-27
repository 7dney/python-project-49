import random
import prompt


def progression():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nFind the greatest"
          f" common divisor of given numbers.")
    n = 0
    while n < 3:
        a = random.randint(1, 5)
        b = random.randint(50, 100)
        c = random.randint(2, 9)

        strange = list(range(a, b, c))
        slic = strange[:10]
        numb_ind = len(slic)
        rand_num_ind = random.randint(1, numb_ind - 1)
        hidden = '''..'''
        greet = slic[rand_num_ind]
        slic.insert(rand_num_ind + 1, hidden)
        slic.pop(rand_num_ind)
        print(' '.join(map(str, slic)))
        user_answer = prompt.string("Your answer: ")
        user_an = int(user_answer)
        if user_an == greet:
            print('Correct!')
        else:
            print(f''''{user_answer}' is wrong answer ;(. Correct'''
                  f"answer was '{greet}'. Let's try again, {user_name}!")
            return
        n = n + 1
    print(f'Congratulations, {user_name}!')
