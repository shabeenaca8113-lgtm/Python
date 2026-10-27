numbers=input("Enter integers separated by spaces:").split()
numbers=[int(n) for n in numbers]
positive=[n for n in numbers if n>0]
print("positive integers:",positive)


