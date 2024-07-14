# Create a class 'Circle' and perform specified methods
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):                           # Calculate the area of the circle
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):                     # Calculate the perimeter of the circle
        return 2 * math.pi * self.radius

    def get_circumference(self):
        return self.get_perimeter()  # Circumference and perimeter are the same for a circle

# Input:
circle = Circle(int(input("Enter 'x' coordinates: ")), int(input("Enter y coordinates: ")), int(input("Enter the radius: ")))
print(f"Area: {round(circle.get_area(), 3)}")
print(f"Perimeter: {round(circle.get_perimeter(), 3)}")
print(f"Circumference: {round (circle.get_circumference(), 3)}")
