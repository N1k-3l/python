class Korzina():
    def __init__(self, capasity):
        self.capasity = capasity
        self.storage = []
        print(f'Создали {self.__class__.__name__} c вместимостью {self.capasity}')
    def put_in(self, item):
        if item.weight <= self.capasity: 
            self.storage.append(item.mark)
            self.capasity -= item.weight
            print(f'Add {item.mark}, в этом {self.__class__.__name__} осталось {self.capasity}')
        else:
            print(f'Вес {item.mark} ({item.weight}), больше  оставшейся вместимости этого {self.__class__.__name__} {self.capasity}')

class Packet(Korzina):
    pass

class Product(object):
    def __init__(self, mark, weight):
        self.weight = weight
        self.mark = mark



zola = Korzina(8)
zara = Packet(5)

dosya = Product('dosya', 3)
piva = Product('pivo', 2)
soap = Product('soap', 1)

zola.put_in(dosya)
print('zola после добавления dosya:')
print(zola.storage)

zola.put_in(piva)
zola.put_in(piva)
zola.put_in(piva)
zola.put_in(piva)
zola.put_in(soap)
print('zola',zola.storage)

print('zara', zara.storage)
zara.put_in(piva)
zara.put_in(piva)
zara.put_in(piva)
print('zara', zara.storage)

input('enter to exit')