def add(*args):
  
    total = 0
    for n in args:
        total = total + n
    return total

numbers=input("Enter integers separated by spaces:").split()
numbers=list(map(int,numbers))

print("Sum=",add(*numbers))
