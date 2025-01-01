class Car:
    def __init__(self, make):
        self.make = make
    def getCar(self):
        print(self.make)

mycar = Car('Tesla')
newcar = Car('Toyota')

mycar.getCar() 
newcar.getCar()
 