import prompt


def welcome_user(Condition):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    if Condition:
        print(f'{Condition}')
    return user_name


def go_answer(question):
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ")
    return user_answer
