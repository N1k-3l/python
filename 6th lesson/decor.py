from functools import wraps, reduce
import time


def decorator_cancel(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f'{func.__name__} is canceled!')
    return inner

def how_much_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        run_func = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} is running for {end - start}')
    return inner

@decorator_cancel
def minus(x, y):
    return x - y


minus(2, 1)

@how_much_time
def squared(n):
    time.sleep(1)
    print(f'n*n={n*n}')
    return n*n


squared(20)


# При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
example_list = [1, 4, 5, 30, 99]
example = list(map(lambda x: x%5, example_list))
print(example)

# При помощи map превратить все числа из массива [3, 4, 90, -2] в строки
list2 = [3, 4, 90, -2]
str_mass = list(map(str, list2))
print(str_mass)
for i in str_mass:
    print(type(i))

# При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки

list3 = ['some', 1, 'v', 40, '3a', str]
print(list3)
filtred_list3 = list(filter(lambda x: isinstance(x, str), list3))
print(filtred_list3)

# При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']

list4 = ['some', 'other', 'value']
reduced_list4 = list(reduce(len(), list4))
print(reduced_list4)