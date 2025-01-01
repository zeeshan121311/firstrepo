class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Initialize attributes
        self.model = model
        self.year = year
    def get(self):
        print(self.brand)
        print(self.model)
        print(self.year)

# Create objects with attributes initialized

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesa", "Model S", 2023)
car3 = Car("BMW", "Model Z", 2024)

car1.get()
car2.get()
car3.get()