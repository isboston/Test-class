li = [1, 2, 3, 4, 5, -4, 6, 10]
summ = 0
for li_item in li:
    if li_item % 2 == 0:
        summ += 1
print(summ)
count = 0
summ = 0
while count < len(li):
    if li[count] % 2 == 0:
        summ += 1
    count += 1
print(summ)
