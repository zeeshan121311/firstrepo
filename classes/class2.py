class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Initialize attributes
        self.model = model
        self.year = year

# Create objects with attributes initialized

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesa", "Model S", 2023)
car3 = Car("BMW", "Model Z", 2024)

print(car1.brand,car1.model,car1.year)
print(car2.brand,car2.model,car2.year)
print(car3.brand,car3.model,car3.year) 