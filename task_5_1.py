while True:
    x = float(input('Enter first number: \n'))
    y = float(input('Enter second number: \n'))
    sign = input('Enter a sign (for example: +, -, *, /): \n')
    if sign == '+':
        z = x + y
        print(z)
    elif sign == '-':
        z = x - y
        print(z)
    elif sign == '*':
        z = x * y
        print(z)
    elif sign == '/':
        if y == 0:
            print('Should not be divided by zero')
        elif y != 0:
            z = x / y
            print(z)
    else:
        print('You entered the sign incorrectly')
