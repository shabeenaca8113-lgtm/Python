def interest(p, t, senior):
    if senior == "Yes":
        r = 12
    else:
        r = 10
    return (p * t * r) / 100

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
senior = input("Senior citizen (Yes/No): ")

print("Simple interest:", interest(p, t, senior))

