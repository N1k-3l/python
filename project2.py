#Создать лист из 6 любых чисел. Отсортировать его по возрастанию

list1 = [534, 53, 23, 6, 98, 13, 0]
list1.sort()
print(list1)


#Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

dict1 = {1:'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i in dict1:
    print(i, dict1[i])

#Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

t = (1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.01, 0.1)
print('max = ', max(t))
print('min = ', min(t))

#Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'

l = ['Earth', 'Russia', 'Moscow']
# l.reverse()
# m = ''
# for i in l:
#     m = i + m
# print(m)
print(l[0], ' -> ', l[1], ' -> ', l[2])


#Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
text =  '/bin:/usr/bin:/usr/local/bin'
list1 = text.split(':')
print(list1)

#Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
for i in range(1,100):
    if i % 7 == 0:
        print(i, ' - multiply 7')
    else:
        print(i, ' - not multiply 7')
#Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

for i in range(10, 0, -1):
    print(i)

#Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

mtrx = [
[1, 2, 3],
[10, 20, 30],
[4, 8, 32],
[5, 15, 75]]
for i in mtrx:
    print(i)
transposed = []


#Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

list1 = [1, 2, 'spaghetti', (1, 2, 3), 'mom']
for i in list1:
    print(i, ':', list1.index(i))



#Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

dele = ['to-delete', 'lol', 'to-delete', 'kek', 'to-delete', 'no-delete']
for i in dele:
    if i == 'to-delete':
        dele.remove(i)
print(dele)
