class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some animal sound...")

# Наследники
class Lion(Animal):
    def make_sound(self):
        print("Roar! 🦁")

class Monkey(Animal):
    def make_sound(self):
        print("Ooh-ooh! 🐒")

class Elephant(Animal):
    def make_sound(self):
        print("Trumpet! 🐘")

# Создаём объекты
lion = Lion("Симба", 5)
monkey = Monkey("Джордж", 2)
elephant = Elephant("Дамбо", 10)

# Вызываем звуки
lion.make_sound()      # Roar! 🦁
monkey.make_sound()    # Ooh-ooh! 🐒
elephant.make_sound()  # Trumpet! 🐘
 