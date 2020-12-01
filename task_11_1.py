class Dog:
    def __init__(self, height, weight, name, age):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age

    def jump(self):
        return 'Dog jumping'

    def run(self):
        return 'Dog running'


class Table:
    def __init__(self, material, weight, stability):
        self.__material = material
        self.__weight = weight
        self.__stability = stability

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material):
        self.__material = material

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def stability(self):
        return self.__stability

    @stability.setter
    def stability(self, stability):
        self.__stability = stability

    def crack(self):
        return 'The crack appeared'

    def fall(self):
        return 'The table fall'
