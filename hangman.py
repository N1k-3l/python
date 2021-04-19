import random
import sys
# vars
SECRETWORDS = ['aquamarine', 'butthurt',
               'cinderella', 'deltaplane', 'fireproof']
PLAYWORD = list(random.choice(SECRETWORDS))
EMPTY_ = []
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
ATTEMPTS = 0

# functions
# find indexes in secret


def check(p, l):
    indexes = [index for index, element in enumerate(p) if element == l]
    return indexes
# push letters to empty


def push(*indexes):
    for i in indexes:
        EMPTY_[i] = U_LETTER


for i in PLAYWORD:
    EMPTY_.append('_')


# print('\n\n', '|'.join(EMPTY_), '\n\n')

while EMPTY_ != PLAYWORD:
    print(HANGMANPICS[ATTEMPTS])
    print('|'.join(EMPTY_))
    U_LETTER = str.lower(input('Enter the letter:\n'))
    t = check(PLAYWORD, U_LETTER)
    if t == []:
        ATTEMPTS += 1
    else:
        push(*t)
    if ATTEMPTS > 5:
        print(HANGMANPICS[ATTEMPTS])
        print('R.I.P')
        sys.exit()
print(
	'''\n \n
█▄████─█▄████─█▄████
▀▀─▄█▀─▀▀─▄█▀─▀▀─▄█▀
──▄██────▄██────▄██
─▄██▀───▄██▀───▄██▀
─███────███────███

    ''')