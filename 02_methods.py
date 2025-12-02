class Circle:

    pi = 3.14

    def __init__(self, radius): # Constructor
        self.radius = radius

    def circum(self):   # Instance method
        return 2 * Circle.pi * self.radius
    
    def area(self): # Instance method
        return Circle.pi * self.radius ** 2
    
    @classmethod    # Class method
    def radius_from_string(cls, radius):
        return cls(float(radius))
    
    @staticmethod   # Static method
    def diameter(radius):
        return 2 * radius
    
print(Circle.pi) # Accessing class variable

circle1 = Circle(5) # Creating an instance of the class
print(circle1.radius)  # Accessing instance variable
print(circle1.circum()) # Calling instance method
print(circle1.area()) # Calling instance method
print(circle1.pi) # Accessing class variable via instance

circle2 = Circle.radius_from_string("7.5")  # Using class method to create an instance
print(circle2.radius)   # Accessing instance variable
print(circle2.circum()) # Calling instance method

print(Circle.diameter(10))  # Using static method