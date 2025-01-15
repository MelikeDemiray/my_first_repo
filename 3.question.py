#Question3: Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.

#Let the "shape" class have two properties: "width" and "height."
#Let the "Rectangle" class inherit from the "Shape" class and add an additional "calculate_area()" method.
#Let the "Square" class inherit from the "Shape" class and calculate the area of ​​the square using the same "area_calculate()" method.
#Create a "Rectangle" and a "Square" instance, determine the width and height of each, and calculate the area of ​​each and print the results.

class Shape():

    def __init__(self, width, height):
        self.width=width
        self.height=height  

class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height
    
class Square(Shape):
    def calculate_area(self):
        return self.width ** 2
    
rectangle = Rectangle(30, 2)
square = Square(3, 3)

print(rectangle.calculate_area())
print(square.calculate_area())
