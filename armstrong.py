def armstrong(n):
    temp = n
    total = 0
    power = len(str(n))

    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10

    if total == n:
        return True
    else:
        return False


