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
TEXT_WIN = '''\n You win!\n
█▄████─█▄████─█▄████
▀▀─▄█▀─▀▀─▄█▀─▀▀─▄█▀
──▄██────▄██────▄██
─▄██▀───▄██▀───▄██▀
─███────███────███'''
# functions



def check(p, l):
    indexes = [index for index, element in enumerate(p) if element == l]
    return indexes
    # find indexes in secret



def push(indexes):
    print(indexes)
    for i in indexes:
        EMPTY_[i] = U_LETTER
    # push letters to empty

def enter_letter():
    while True:
        letter = str.lower(input('Enter the letter:\n'))
        if letter.isalpha():
            return letter
    # letter input and check


for i in PLAYWORD:
    EMPTY_.append('_')

while EMPTY_ != PLAYWORD:
    print(HANGMANPICS[ATTEMPTS])
    print('|'.join(EMPTY_))
    U_LETTER = enter_letter()
    t = check(PLAYWORD, U_LETTER)
    if t == []:
        ATTEMPTS += 1
    else:
        push(t)
    if ATTEMPTS > 5:
        print(HANGMANPICS[ATTEMPTS])
        print('R.I.P')
        print(PLAYWORD)
        sys.exit()
print(TEXT_WIN)
