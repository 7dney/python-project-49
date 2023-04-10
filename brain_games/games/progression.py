import random


CONDITION = 'What number is missing in the progression?'


def get_question_and_right_answer():
    start = random.randint(1, 4)
    stop = random.randint(60, 100)
    step = random.randint(2, 7)

    strange = list(range(start, stop, step))
    slic = strange[:10]
    numb_ind = len(slic)
    rand_num_ind = random.randint(1, numb_ind - 1)
    hidden = ".."
    greet = slic[rand_num_ind]
    slic.insert(rand_num_ind + 1, hidden)
    slic.pop(rand_num_ind)
    question = ' '.join(map(str, slic))
    return question, str(greet)
