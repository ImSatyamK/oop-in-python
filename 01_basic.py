class Cal_circle:

    pi = 3.14   # class variable

    def __init__(self, radius): # Constructor
        self.radius = radius  # instance variable

    def circum(self):   # Instance method
        return 2*self.pi*self.radius
    
    def area(self):  # Instance method
        return self.pi*self.radius**2


print(Cal_circle.pi)

circle1 = Cal_circle(5)
print(circle1.radius)
print(circle1.circum())
print(circle1.area())
print(circle1.pi)