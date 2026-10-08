names=input("Enter first names separated by spaces:").split()
count=0
for name in names:
    count +=name.lower().count('a')
print("Number of occurences of 'a':",count)
