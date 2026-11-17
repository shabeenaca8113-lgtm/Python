import armstrong

start = int(input("Enter lower limit: "))
end = int(input("Enter upper limit: "))

print("Armstrong numbers are:")

for i in range(start, end + 1):
    if armstrong.armstrong(i):
        print(i)
