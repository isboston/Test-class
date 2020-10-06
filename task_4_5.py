first_number = int(input('Enter the first number:\n'))
second_number = first_number
new_li = [first_number, second_number]
while len(new_li) < 15:
    sum_two_number = first_number + second_number
    new_li.append(sum_two_number)
    first_number = second_number
    second_number = sum_two_number
print(new_li)

first_number = int(input('Enter the first number:\n'))
second_number = first_number
new_li = [first_number, second_number]
for i in range(2, 15):
    sum_two_number = first_number + second_number
    new_li.append(sum_two_number)
    first_number, second_number = second_number, sum_two_number
print(new_li)
