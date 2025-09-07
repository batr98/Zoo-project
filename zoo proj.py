class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed(self):
        print("Some animal food...")
class Lion(Animal):
    def feed(self):
        print("lion is being fed with meat.")
class Monkey(Animal):
    def feed(self):
        print("Monkey is being fed with bananas.")
class Elephant(Animal):
    def feed(self):
        print("Elephant is being fed with grass.")
lion = Lion("meat",5)
monkey=Monkey("bananas",6)
elephant=Elephant("grass",7)
lion.feed()       
monkey.feed()     
elephant.feed()   

