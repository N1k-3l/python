from math import sqrt
import sys

def vvod():
    while True:
        abc = list(input('введите стороны фигуры через пробел: ').split())
        if abc != []:
            if check(abc):
                abc_int = list(map(int, abc))
                return abc_int
        print('вводите только числа!')

def check(listok):
    RESPONCE = True
    for symb in listok:
        if not symb.isdigit():
            RESPONCE = False
    return RESPONCE

def isnt_real_check(sides):
    """a + b > c, b + c > a, a + c > b."""
    if ((sides[0] < (sides[1] + sides[2]))
    and (sides[1] < (sides[2] + sides[0]))
    and (sides[2] < (sides[0] + sides[1]))):
        return True

def main():
    while True:
        vvod_storon = vvod()
        if len(vvod_storon) in RULES:
            while True:
                if len(vvod_storon) == 3 and not isnt_real_check(vvod_storon):
                    print('такой треугольник построить нельзя')
                    main()
                FIGURE = RULES[len(vvod_storon)](vvod_storon)
                FIGURE.output()
                input('press any key to exit')
                sys.exit()
        print('введите от 1 до 4 сторон!')

class Tetragon(object):
    name = 'Tetragon'
    def __init__(self, arg):
        self.sides = arg
        self.arg = arg

    def square(self):
        S = 'Oooops!'
        return S

    def perimeter(self):
        P = sum(self.sides)
        return P
    
    def print_result(self, S, P):
        print(f'For this {self.name} S: {S}, P: {P}')

    def output(self):
        self.print_result(self.square(), self.perimeter())

class Rectangle(Tetragon):
    name = 'Rectangle'
    def __init__(self, arg):
        self.sides = arg * 2
        self.arg = arg

    def square(self):
        S = self.arg[0] * self.arg[1]
        return S


class Quadrant(Rectangle):
    name = 'Quadrant'
    def __init__(self, arg):
        self.sides = arg * 4
        self.arg = arg
    def square(self):
        return self.arg[0] * self.arg[0]

class Triangle(Tetragon):
    name = 'Triangle'
    def __init__(self, arg):
        self.sides = arg
    #     ''''''
    #     if not self.isnt_real_check():
    #         raise ValueError('This isn\'t Triangle')

    # def isnt_real_check(self):
    #     """a + b > c, b + c > a, a + c > b."""
    #     if ((self.sides[0] < (self.sides[1] + self.sides[2]))
    #     and (self.sides[1] < (self.sides[2] + self.sides[0]))
    #     and (self.sides[2] < (self.sides[0] + self.sides[1]))):
    #         return True

    def square(self):
        p = self.perimeter() / 2
        S = sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
        return S

RULES = {1:Quadrant, 2:Rectangle, 3:Triangle, 4:Tetragon}


T = [2, 2, 2]

T2 = [3, 4, 5]

t = Triangle(T)
t2 = Triangle(T2)

main()
