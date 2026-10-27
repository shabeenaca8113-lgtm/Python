numbers=list(map(int,input("Enter numbers separated by spaces:").split()))
total=0
for n in numbers:
    total=total+n
print("sum of all items:",total)
