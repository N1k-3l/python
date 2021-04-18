import random
from random import randint
###


def coord(el, mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] == el:
                return (i, j)


def pri(a):
    for i in a:
        print(' '.join(map(str, i)))
    print(' \n \n')


def a_move(a):
    print("#[a]\n")
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i][j - 1]
        mtrx[i][j - 1] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        print('STOP MOVE LEFT!!! \n \n')
        pass
    pri(mtrx)
    return a


def d_move(a):
    print('#[d] \n')
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i][j + 1]
        mtrx[i][j + 1] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        print('STOP MOVE RIGHT!!! \n \n')
        pass
    pri(mtrx)
    return a


def s_move(a):
    print('#[s] \n')
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i + 1][j]
        mtrx[i + 1][j] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        print('STOP MOVE DOWN!!! \n \n')
        pass
    pri(mtrx)


def w_move(a):
    print('#[w] \n')
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i - 1][j]
        mtrx[i - 1][j] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        print('STOP MOVE UP!!! \n \n')
        pass
    pri(mtrx)
##


#i = randint(0, 3)
#j = randint(0, 3)

#mtrx = [
#     ['01', '02', '03', '04'],
#     ['05', '06', '07', '08'],
#     ['09', '10', '11', 'XX'],
#     ['13', '14', '15', '12']]

win_mtrx = [
    ['01', '02', '03', '04'],
    ['05', '06', '07', '08'],
    ['09', '10', '11', '12'],
    ['13', '14', '15', 'XX']]

mtrx = win_mtrx
for string_ in mtrx:
    random.shuffle(string_)

#temp = mtrx[i][j]
#mtrx[i][j] = 'XX'
#mtrx[3][3] = temp

win_mtrx = [
    ['01', '02', '03', '04'],
    ['05', '06', '07', '08'],
    ['09', '10', '11', '12'],
    ['13', '14', '15', 'XX']]
pri(mtrx)

i = (coord('XX', mtrx))[0]
j = ((coord('XX', mtrx))[1])
pri(win_mtrx)
while mtrx != win_mtrx:
    move = input('Enter your move!  (use w, a, s, d)\n:')
    if move == 'w':
        if i != 0:
            w_move(mtrx)
            i = (coord('XX', mtrx))[0]
            j = ((coord('XX', mtrx))[1])
        else:
            print('STOP MOVE UP!!! \n \n')
            pri(mtrx)
    elif move == 'd':
        d_move(mtrx)
        i = (coord('XX', mtrx))[0]
        j = ((coord('XX', mtrx))[1])
    elif move == 's':
        s_move(mtrx)
        i = (coord('XX', mtrx))[0]
        j = ((coord('XX', mtrx))[1])
    elif move == 'a':
        if j != 0:
            a_move(mtrx)
            i = (coord('XX', mtrx))[0]
            j = ((coord('XX', mtrx))[1])
        else:
            print('STOP MOVE LEFT!!! \n \n')
            pri(mtrx)
    else:
        print('Use w, a, s, d keys only!')
print('You win \n TA DA !!! \n \\ (•◡•) /')
