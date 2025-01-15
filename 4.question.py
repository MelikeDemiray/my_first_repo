#Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

#Features:
#"make" (Brand of vehicle)
#"model" (Vehicle model)
#"year" (Year of manufacture of the vehicle)
#Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

#The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
#Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.
#Create an instance of each class, determine its properties, and write a program to display these properties.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Off_Road_Vehicle(Vehicle):
    def __init__(self,make,model,year,four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive=four_wheel_drive

class SportCar(Vehicle):
    def __init__(self,make,model,year,max_speed):
        super().__init__(make, model, year)
        self.max_speed=max_speed


off_road=Off_Road_Vehicle("Toyota", "Land Cruiser", 2021, True)
sportCar=SportCar("Ferrari", "488 GTB", 2022, 330)

print("Off-Road Vehicle Info:")
print(f"Make: {off_road.make}, Model: {off_road.model}, Year: {off_road.year}, Four-Wheel Drive: {off_road.four_wheel_drive}")

print("\nSports Car Info:")
print(f"Make: {sportCar.make}, Model: {sportCar.model}, Year: {sportCar.year}, Max Speed: {sportCar.max_speed} km/h")
