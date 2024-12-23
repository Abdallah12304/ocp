# from abc import ABC, abstractmethod
# # Abstract Class
# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#     @abstractmethod
#     def drive(self):
#         pass
# # Concrete Class 1
# class Car(Vehicle):
#     def start_engine(self):
#         print("Starting car engine with key")
#     def drive(self):
#         print("Driving the car on the road")
# # Concrete Class 2
# class ElectricScooter(Vehicle):
#     def start_engine(self):
#         print("Starting electric scooter with button")
#     def drive(self):
#         print("Driving the scooter on the sidewalk")
# # Create instances
# car = Car()
# scooter = ElectricScooter()
# # Use abstraction
# for vehicle in (car, scooter):
#     vehicle.start_engine()
#     vehicle.drive()
#!##################################################################################################
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14159 * self.radius ** 2
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
# rectangle = Rectangle(4, 5)
# circle = Circle(3)
# triangle = Triangle(6, 4)
# print(f"The area of the rectangle is: {rectangle.area()}")
# print(f"The area of the circle is: {circle.area()}")
# print(f"The area of the triangle is: {triangle.area()}")
#!###################################################################################################
