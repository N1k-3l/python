ra = 0 
name =  str.capitalize(input('What is your name? \n'))
if name == "":
    name = 'Anonimus'
print('Hello, {}!'.format(name))
a = str.lower(input('You understand first lesson?\n'))
if a in 'yes,да' and a != "":
    ra += 1
a = str.lower(input('What is course name?\n'))
if a in 'python,питон' and a != "":
    ra += 1
a = str.lower(input('Result of \'12\' + \'5\' ?\n'))
if a == '125':
    ra += 1
a = str.lower(input('Result of 7 == 9?\n'))
if a == 'false':
    ra += 1
a = input('Result of 3 + 5 ?\n')
if a == '8':
    ra += 1
print('{}, you have {} right answers! '.format(name, ra))
