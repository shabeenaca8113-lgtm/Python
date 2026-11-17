from graphics.rectangle import *

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

print("Rectangle area:", area(l, b))
print("Rectangle perimeter:", perimeter(l, b))


from graphics.circle import *

r = int(input("Enter radius: "))

print("Circle area:", area(r))
print("Circle perimeter:", perimeter(r))


from graphics.cuboid import *

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))

print("Cuboid area:", area(l, b, h))
print("Cuboid perimeter:", perimeter(l, b, h))


from graphics.sphere import *

r = int(input("Enter radius: "))

print("Sphere area:", area(r))
print("Sphere perimeter:", perimeter(r))
