class Pet:
    __counter = 0

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__counter += 1

    @classmethod
    def get_counter(cls):
        return cls.__counter

    def change_weight(self, diff=0.2):
        self.weight += diff

    def change_height(self, height):
        self.height = height
        if height:
            self.height = height
        else:
            self.height += 0.2

    def voice(self):
        pass

    def run(self):
        print("Run!")

    def jump(self, height):
        print(f"Jump\n{height}!")

    def sleep(self):
        print("Sleep...")

    def birthday(self):
        self.age += 1


class Dog(Pet):
    def voice(self):
        print("Woof-woof")

    def jump(self, height):
        if height > 0.5:
            print("Dogs cannot jump so high")
        else:
            super().jump(height)


class Cat(Pet):
    def voice(self):
        print("Meow")

    def jump(self, height):
        if height > 0.5:
            print("Cats cannot jump so high")
        else:
            super().jump(height)


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def voice(self):
        print("You dummy")

    def fly(self):
        if self.weight > 0.1:
            print("This parrot cannot fly")
        else:
            print("Flies away...")

    def jump(self, height):
        if height > 0.5:
            print("Parrots cannot jump so high")
        else:
            super().jump(height)

    def change_weight(self, diff=0.05):
        self.weight += diff

    def change_height(self, height=0.05):
        self.height += height


def animals_voice(animals):
    for animal in animals:
        animal.voice()


parrot = Parrot("Tepa", 3, "Pumba", 0.2, 10, "Some parrot")
parrot.jump(0.6)

dog = Dog("Fuf", 3, "Pumba", 5, 50)
dog.jump(0.5)

cat = Cat("Tepa", 3, "Pumba", 4, 30)
animals_voice([dog, parrot, cat])
