for num in range(200, 300):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if s > num:
        result = 0
        for i in range(1, s):
            if s % i == 0:
                result += i
        if result == num:
            print(num, s)
