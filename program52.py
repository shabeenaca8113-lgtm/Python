
class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __add__(self, other):
        total_seconds = (self.__hours * 3600 + self.__minutes * 60 + self.__seconds) + (other.__hours * 3600 + other.__minutes * 60 + other.__seconds)

        h = total_seconds // 3600
        total_seconds %= 3600
        m = total_seconds // 60
        s = total_seconds % 60

        return Time(h, m, s)

    def display(self):
        print(self.__hours, "hours", self.__minutes, "minutes", self.__seconds, "seconds")


# Get first time
print("Enter first time:")
h1 = int(input("Enter hours: "))
m1 = int(input("Enter minutes: "))
s1 = int(input("Enter seconds: "))

t1 = Time(h1, m1, s1)

# Get second time
print("\nEnter second time:")
h2 = int(input("Enter hours: "))
m2 = int(input("Enter minutes: "))
s2 = int(input("Enter seconds: "))

t2 = Time(h2, m2, s2)

# Add two time objects
t3 = t1 + t2

print("\nFirst Time:")
t1.display()

print("Second Time:")
t2.display()

print("Sum of two times:")
t3.display()

