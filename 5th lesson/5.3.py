class Animal(object):
    """Use 2 arguments if Animal is dangerous """
    def __init__(self, name, dangerous = False):
        self.dangerous = dangerous
        self.name = name

class Human():
    """Specify race if necessary"""
    dangerous = True
    def __init__(self, race = None):
        self.race = race
    def is_dangerous(self, animal):
        if animal.dangerous:
            if animal.__class__ == Human:
                animal.name = 'Human'
            print(f'This {animal.name} is dangerous for Human! ({animal.dangerous})')
        else:
            print(f'This {animal.name} is friendly for Human!')


Snake = Animal('Snake', 'Poison')
Sparrow = Animal('Sparrow')
Tiger = Animal('Tiger', 'Predator')
Crocodile = Animal('Crocodile', 'Aggressive')
Cat = Animal('Cat')

Eva = Human('European')

Eva.is_dangerous(Snake)
Eva.is_dangerous(Sparrow)
Eva.is_dangerous(Tiger)
Eva.is_dangerous(Crocodile)
Eva.is_dangerous(Cat)

