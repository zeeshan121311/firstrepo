class Dog:
    # Constructor (Initializer)
    def __init__(self, name, bread):
        self.name = name   # Instance Variable
        self.bread = bread   # Instance Variable

        # Method (Behavior)
        def bark(self):
            print(f"{self.name} says Woof!")

        def get_breed(self):
            return self.bread
 
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Bulldog")

# Accessing Attributes
print(dog1.name)
print(dog2.name)
print(dog1.bread)
print(dog2.bread)