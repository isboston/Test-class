number = int(input('Enter a number:\n'))
sum_number = 0
mul_number = 1
while number > 0:
    digit = number % 10
    sum_number = sum_number + digit
    mul_number = mul_number * digit
    number = number // 10
print(f'sum_of_number: {sum_number}, mul_of_number: {mul_number}')
