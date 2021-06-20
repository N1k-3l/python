import random

def random_():
    '''вывод рандомного числа'''
    while True:
        yield random.randint(1, 100)

def range_(start, stop, step = 1):
    """генератор работающий как range()"""
    while start < stop:
        yield start
        start += step

def map_(funct, iterable):
    """генератор работающий как map()"""
    for i in iterable:
        yield funct(i)

def enumerate_(iterable):
    '''генератор работающий как enumerate()'''
    number = 0
    for i in iterable:
        yield number, i
        number += 1

def zip_(iterable, iter2=[]):
    '''генератор работающий как zip()'''
    length = min((len(iterable), len(iter2)))
    for i in range(length):
        yield iterable[i], iter2[i]