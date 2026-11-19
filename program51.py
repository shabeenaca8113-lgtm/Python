
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


print("--- First Rectangle ---")
l1 = float(input("Enter length: "))
b1 = float(input("Enter breadth: "))
r1 = Rectangle(l1, b1)


print("\n--- Second Rectangle ---")
l2 = float(input("Enter length: "))
b2 = float(input("Enter breadth: "))
r2 = Rectangle(l2, b2)


print("\nFirst Rectangle")
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print("\nSecond Rectangle")
print("Area:", r2.area())
print("Perimeter:", r2.perimeter())


print("\n--- Comparing Rectangles ---")
if r1.area() > r2.area():
    print("First rectangle has greater area.")
elif r1.area() < r2.area():
    print("Second rectangle has greater area.")
else:
    print("Both rectangles have equal area.")

