class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self, msg):
        return f"{self.name} says {msg}"

class Cat(Animal):

    pass

class Dog(Animal):

    def sound(self, msg):
        return f"{self.name} woofs {msg}"

    def __str__(self):
        return f"{self.name} is {self.age} year old ({super().__str__()})"


if __name__ == '__main__':
    dog = Dog('Luna', 1)
    print(dog)
    # print(dog == Dog)
    # print(dog.__class__ == Dog)
    # print(dog.__class__ == Animal)
    # print(isinstance(dog, Animal))
    # animal = Animal('Kiki', 3)
    # print(animal.sound('hi'))
    # cat = Cat('Lily', 2)
    # print(cat.sound('hello'))
    # dog = Dog('Luna', 1)
    # print(dog.sound('haha'))

