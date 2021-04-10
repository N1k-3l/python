#1
print('#1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError.Обрабатываем ошибку, говорим пользователю, в чем его ошибка')

x = int(input('Can you enter a number? \n'))
try:
    if x % 2 == 0:
        raise ValueError('Even number! \n ( ⚆ _ ⚆ )')
    if x < 0:
        raise TypeError('Less than zero!')
    if x > 10:
        raise IndexError('Greater than 10!')
except IndexError as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
print('#2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. Если все хорошо - пишите объект в консоль. Если нет - обработайте возмозможные ошибки и скажите ему, что не так')

import random
list1 = random.sample(range(100), 5)
print(list1)
x = int(input('Enter a number \n'))
try:
    if x >= 0:
        if x <= len(list1):
            print(list1[x])
        else:
            raise IndexError('Too much!')
    else:
        raise IndexError('Negative')
except IndexError as e:
    print(e)

print('#2/1.Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0')

def function1(a,b):
    if a < 0 and b < 0:
    	return (a - b)
    elif a > 0 and b > 0:
        return (a + b)
    else:
        return 0
x, y = map(int, input('enter 2 numbers \n').split( ))
print(function1(x, y))

print('#2/2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль')

def function2(a, b, c):
    ret = [a, b, c]
    ret.remove(min(ret))
    return ret

x, y, z = map(int, input('enter 3 numbers \n').split( ))
returnf = function2(x, y, z)
print(returnf[0], returnf[1])













