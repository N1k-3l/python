r = 0
name =  str.capitalize(input('What is your name? \n'))
if name == "":
    name = 'Anonimus'
t  = {'You understand first lesson?\n':'yes', 'What is course name?\n':'python', 'Result of \'12\' + \'5\' ?\n':'125', 'Result of 7 == 9?\n':'false', 'Result of 3 + 5 ?\n':'8'}
for a, b in t.items():
    c = str.lower(input(a))
    if c == b:
        r += 1
print('{}, you have {} right answers! '.format(name, r))