import random

FIELD = list(range(1,10))
X_SIDE = 'X'
O_SIDE = '0'
def print_field(field):
    print(''' \n\n
---------''')
    for i in range(0, 9, 3):
        print((FIELD[i:i+3]))
        print('---------')
    print('\n\n')

def game_end():
    return True

def turn(field):
    try:
        key = int(input('Input 1-9 to put on X:'))
        if key in field:
            field[key-1] = X_SIDE
            return field
        raise ValueError
    except ValueError:
       print('Error move!')

def comp_turn(field):
    valid_moves = [index for index, element in enumerate(field) if element != X_SIDE]
    print(valid_moves)
    field[(random.choice(valid_moves))] = O_SIDE

def main():
    while game_end():
        print_field(FIELD)
        turn(FIELD)
        comp_turn(FIELD)
main()