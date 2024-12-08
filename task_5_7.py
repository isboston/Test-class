li = [[1, 2, 3, 1], [4, 5, 6, 8], [7, 8, 9, 6], [6, 3, 2, 2]]
for i in li:
    print(i)
li_index = 0
while li_index < len(li):
    column_index = 0
    li_max = 0
    max_index = 0
    while column_index < len(li[li_index]):
        if li[li_index][column_index] > li_max:
            li_max = li[li_index][column_index]
            max_index += 1
        column_index += 1
    temp = li[li_index][li_index]
    li[li_index][li_index] = li_max
    li[li_index][max_index - 1] = temp
    li_index += 1
print('_______________')
for i in li:
    print(i)
