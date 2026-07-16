class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self, msg):
        return f"{self.name} says {msg}"


if __name__ == '__main__':
    animal = Animal('Kiki', 3)
    print(animal.sound('hi'))

