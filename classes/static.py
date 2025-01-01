class mathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
# Calling Static Method without creating an instance of the class

print(mathUtils.add(2,3))   # Outhput: 5
print(mathUtils.multiply(2,3))   # Outhput: 6
