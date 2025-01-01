class Car:
    def __init__(self, brand, model, year):
        self.brand = brand # Initialize attributes
        self.model = model
        self.year = year
    def start(self):
        print(f"{self.brand} {self.model} {self.year} is starting!")

    def stop(self):
        print(f"{self.brand} {self.model} {self.year} is stopping!")

# Create an objects

my_car1 = Car("Toyota", "Corolla", 2022)
my_car2 = Car("Tesa", "Model S", 2023)
my_car3 = Car("BMW", "Model Z", 2024)

my_car1.start()
my_car1.stop()
my_car2.start()
my_car3.start()
my_car3.stop() 