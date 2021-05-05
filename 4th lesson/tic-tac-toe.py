import random
import sys

FIELD = list(range(1,10))
X_SIDE = 'X'
O_SIDE = 'O'

def print_field(field):
    print(''' \n
---------''')
    for i in range(0, 9, 3):
        print((FIELD[i:i+3])) 
        print('---------')
    print('\n')

def game_end(field):
    if field[0] == field[4] == field[8] or field[2] == field[4] == field[6]:
        print('\nWinner is ', field[4])
        return False
    for i in range(0, 9, 3):
        if field[i] == field[i+1] == field[i+2]:
            print('\nWinner is ', field[i])
            return False
    for i in range(0,3):
        if field[i] == field[i+3] == field[i+6]:
            print('\nWinner is ', field[i])
            return False
    return True

def turn(field):
    while True:
        try:
            key = int(input('Input 1-9 to put on X:'))
            if key in field:
                field[key-1] = X_SIDE
                return field
            raise ValueError
        except ValueError:
            print('Error move!')

def comp_turn(field):
    valid_moves = [index for index, element in enumerate(field) if (element != X_SIDE) and (element != O_SIDE) ]
    if valid_moves != []:
        field[(random.choice(valid_moves))] = O_SIDE
    else:
        print('Draw!')
        sys.exit(0)


def main():
    while game_end(FIELD):
        print_field(FIELD)
        turn(FIELD)
        if game_end(FIELD) == False:
            break
        comp_turn(FIELD)
    print_field(FIELD)
main()