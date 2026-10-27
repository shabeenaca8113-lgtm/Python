n=int(input("Enter number of items:"))
d={}
for i in range(n):
    key=int(input("Enter key:"))
    value=input("Enter value:")
    d[key]=value
asc=dict(sorted(d.items()))
desc=dict(sorted(d.items(),reverse=True))

print("Original dictionaty:",d)
print("Ascending order:",asc)
print("Descending order:",desc)
