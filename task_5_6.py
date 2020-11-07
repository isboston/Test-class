from random import randint
li = [randint(0, 5) for elem in range(0, 10)]
print(li)
result = 0  # number of array list
count = 0
for item in range(len(li) - 1):
    if li[item] < li[item + 1]:
        count += 1
    elif li[item] >= li[item + 1] and count >= 1:
        result += 1
        count = 0
print(result)
