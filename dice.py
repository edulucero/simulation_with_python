#A simulation of rolling n number of dices

def dice(n):
    x = np.random.rand()
    if x < 1/6:
        print('.')
    if x < 2/6 and x > 1/6:
        print('. .')
    if x < 3/6 and x > 2/6:
        print('. . . ')
    if x < 4/6 and x > 3/6:
        print('. . . .')
    if x < 5/6 and x > 4/6:
        print('. . . . .')
    if x < 1 and x > 5/6:
        print('. . . . . .')
