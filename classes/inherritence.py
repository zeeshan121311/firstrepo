class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print(f"{self.name} is speaking")

class Dog(Animal):
    pass

StreetDog = Dog("Tom","Something")
StreetDog.speak()