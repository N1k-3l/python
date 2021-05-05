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

# for shuffle


def a_move_s(a):
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i][j - 1]
        mtrx[i][j - 1] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        pass
    return a


def d_move_s(a):
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i][j + 1]
        mtrx[i][j + 1] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        pass
    return a


def s_move_s(a):
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i + 1][j]
        mtrx[i + 1][j] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        pass


def w_move_s(a):
    MOVE = mtrx[i][j]
    try:
        XX = mtrx[i - 1][j]
        mtrx[i - 1][j] = MOVE
        mtrx[i][j] = XX
    except IndexError:
        pass

###

difficult = str.lower(input('Choose your destiny! (Fingerprint easy or hard): \n'))
if difficult == 'easy':
    diff = 5
    print('Easy game start now!')
else:
    diff = 25
    print('Hard game start now!')
    
moves = []
for i in range(diff):
    moves.append(randint(1, 4))

win_mtrx = [
    ['01', '02', '03', '04'],
    ['05', '06', '07', '08'],
    ['09', '10', '11', '12'],
    ['13', '14', '15', 'XX']]

mtrx = win_mtrx

i = (coord('XX', mtrx))[0]
j = ((coord('XX', mtrx))[1])

# >> Shuffling
for move in moves:
    if move == 1:
        if i != 0:
            w_move_s(mtrx)
            i = (coord('XX', mtrx))[0]
            j = ((coord('XX', mtrx))[1])
    elif move == 2:
        d_move_s(mtrx)
        i = (coord('XX', mtrx))[0]
        j = ((coord('XX', mtrx))[1])
    elif move == 3:
        s_move_s(mtrx)
        i = (coord('XX', mtrx))[0]
        j = ((coord('XX', mtrx))[1])
    elif move == 4:
        if j != 0:
            a_move_s(mtrx)
            i = (coord('XX', mtrx))[0]
            j = ((coord('XX', mtrx))[1])


win_mtrx = [
    ['01', '02', '03', '04'],
    ['05', '06', '07', '08'],
    ['09', '10', '11', '12'],
    ['13', '14', '15', 'XX']]
pri(mtrx)

turns = 0
#
while mtrx != win_mtrx:
    move = input('Enter your move!  (use w, a, s, d)\n:')
    turns += 1
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
        turns -= 1
print('You win \n TA DA !!! \n \\ (•◡•) /')
print('You make ', turns, ' moves')