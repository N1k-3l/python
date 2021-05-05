class Person(object):
    """docstring for Person"""
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.known_persons = {}

    def know(self, person):
        self.known_persons[person.name] = person.age
        print(f'{self.name} knows {person.name} now!')

    def is_known(self, person):
        if (person.name in self.known_persons
        and self.known_persons[person.name] == person.age):
            print(f'{self.name} knows {person.name}')
        else:
            print(f"{self.name} doesn't know {person.name}({person.age})")

Egor = Person('Egor', 20)
Psina = Person('Psina', 25)
Kot = Person('Kot', 10)

print('Egor.known_persons ', Egor.known_persons)
print('Psina.known_persons ', Psina.known_persons)
print('Kot.known_persons ', Kot.known_persons)


Egor.know(Psina)
Psina.know(Kot)
Kot.know(Egor)
Kot.know(Psina)

print('Egor.known_persons ', Egor.known_persons)
print('Psina.known_persons ', Psina.known_persons)
print('Kot.known_persons ', Kot.known_persons)

Egor.is_known(Psina)
Egor.is_known(Kot)
Psina.is_known(Egor)
Psina.is_known(Kot)
Kot.is_known(Psina)
Kot.is_known(Egor)