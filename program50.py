
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Polygon):
    def get_data(self):
        self.length = float(input("Enter length of rectangle: "))
        self.breadth = float(input("Enter breadth of rectangle: "))

    def area(self):
        print("Area of Rectangle:", self.length * self.breadth)


class Triangle(Polygon):
    def get_data(self):
        self.base = float(input("Enter base of triangle: "))
        self.height = float(input("Enter height of triangle: "))

    def area(self):
        print("Area of Triangle:", 0.5 * self.base * self.height)


print("--- Rectangle ---")
r = Rectangle()
r.get_data()
r.area()

print("\n--- Triangle ---")
t = Triangle()
t.get_data()
t.area()

