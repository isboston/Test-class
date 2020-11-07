number = int(input('Enter the number:\n'))
sum_of_numbers = 0
next_n = 0
for i in range(1, number + 1):
    next_n = 1 / i
    sum_of_numbers += next_n
    i += 1
print(sum_of_numbers)
