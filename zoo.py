from abc import ABC,abstractmethod
import random
class Animal(ABC):
    zoo_name = "The Govt Zoo"
    def __init__(self,name,species):
        self.name = name
        self.species = species
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
class Lion(Animal):
    def __init__(self,name,species=""):
        super(). __init__(name,species='Lion')
    def make_sound(self):
        print("Roar!")
    def eat(self):
        print(f"{self.name} eats Meat")
class Monkey(Lion):
    def __init__(self,name):
        super(). __init__(name,species='Monkey')
    def make_sound(self):
        print("ooh aha")
    def eat(self):
        print(f"{self.name} eats Banana")

class Penguin(Animal):
    def __init__(self,name):
        super().__init__(name,species="penguin")
    def make_sound(self):
        print("oohoo")
    def eat(self):
        print(f"{self.name} eats Fish")
    def slide(self):
        print(f"{self.name} slides on its Belly!")

class ZooKeeper:
    def __init__(self,name):
        self.name =name
        self._employee_id = random.randint(1000,9999)
        self.__salary = 45000
    def feed_animals(self,animals):
        self.animal = animals
        self.animal.eat()
        self.animal.make_sound()


animals = [Lion("Shero"),Monkey("Momo"),Penguin("Pagu")]
zoo_handler = ZooKeeper("Hamza")
for animal in animals:
    zoo_handler.feed_animals(animal)
    