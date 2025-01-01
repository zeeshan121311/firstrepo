class dog:
    species = "Canis Familiaris"  # Class Variable , Common to all instances
    
    def __init__(self, name, breed):
        self.name = name   # Instance Variable
        self.breed = breed

# Creating Instances

dog1 = dog("Rex", "Labrador")
dog2 = dog("Bella", "Bulldog")

# Accessing class Variable
print(dog1.species)  # Output: Canis Familiaris
print(dog2.species)  # Output: Canis Familiaris

# Changing the class variable
dog.species = "Canis lupus familiaris"

# All Instances Reflect the change
print(dog1.species) # Output: Canis lupus familiaris
print(dog2.species) # Output: Canis lupus familiaris