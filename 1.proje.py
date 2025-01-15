#Question1: Create a Python class called "Rectangle" that represents a rectangle. 
#The Rectangle class must have the following properties and methods:

#Features:
#width (an integer)
#height (an integer)
#Methods:
#area(self): A method that calculates and returns the area of ​​the rectangle.
#perimeter(self): A method that calculates and returns the perimeter of the rectangle.
#Create an instance of Rectangle class, set its width to 5 and height to 7, then print its area and perimeter.

class Rectangle():

    def __init__(self, width, height):
        self.width=width
        self.height=height  

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width*2) + (self.height*2)
    

x=Rectangle(3,2)

print(f"Rectangle area:{Rectangle.area(x)}\nRectangle perimeter:{Rectangle.perimeter(x)}")