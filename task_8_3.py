def fact(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def sin1(x, e):
    sin_x = x
    while True:
        for n in range(1, 100):
            slag = (-1) ** n * x ** ((2 * n + 1) / fact(2 * n + 1))
            if abs(slag) > e:
                sin_x += slag
            else:
                break
        return sin_x


print(sin1(3, 1))
