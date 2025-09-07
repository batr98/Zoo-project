class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        self.make_sound
class Lion(Animal):
    def feed(self):
        print("lion is being fed with meat.")
class Monkey(Animal):
    def feed(self):
        print("Monkey is being fed with bananas.")
class Elephant(Animal):
    def feed(self):
        print("Elephant is being fed with grass.")
class Zoo:
    def __init__(self):
        self.animals=[]
    def add_animal(self,animal):
        self.animals.append(animal)
        print(f"{animal.name},{animal.age} age.")
    def show_all(self):
        for animal in self.animals:
            print(f"{animal.name},{animal.age} age.")
    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()
lion=Lion("Симба", 5)
monkey=Monkey("aknazar",6)
elephant=Elephant("Dumbo", 7)
lion.make_sound()
monkey.make_sound()
elephant.make_sound()
lion.feed()
monkey.feed()
elephant.feed()

zoo=Zoo()
zoo.add_animal(lion)
zoo.add_animal(monkey)
zoo.add_animal(elephant)
zoo.show_all()
zoo.make_all_sounds()