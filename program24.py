n1=int(input("Enter number of items in first dictionary:"))
d1={}
for i in range(n1):
    key=input("Enter key:")
    value=input("Enter value:")
    d1[key]=value
n2=int(input("Enter number of items in second dictionary:"))
d2={}
for i in range(n2):
    key=input("Enter key:")
    value=input("Enter value:")
    d2[key]=value
d3=d1.copy()
d3.update(d2)
print("first dictionary:",d1)
print("second dictionary:",d2)
print("Merged dictionary:",d3)
