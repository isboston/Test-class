m = int(input('Enter the first number:\n'))
n = int(input('Enter the second number:\n'))
while m <= n:
    index = 2
    list_of_dividers = []
    while index < m:
        if m % index == 0:
            list_of_dividers.append(index)
        index += 1
    print(f'для {m} делители {list_of_dividers}')
    m += 1
