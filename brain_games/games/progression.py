import random


Condition = 'What number is missing in the progression?'


def funct_game():
    a = random.randint(1, 4)
    b = random.randint(60, 100)
    c = random.randint(2, 7)

    strange = list(range(a, b, c))
    slic = strange[:10]
    numb_ind = len(slic)
    rand_num_ind = random.randint(1, numb_ind - 1)
    hidden = '''..'''
    greet = slic[rand_num_ind]
    slic.insert(rand_num_ind + 1, hidden)
    slic.pop(rand_num_ind)
    strang = ' '.join(map(str, slic))
    return strang, str(greet)