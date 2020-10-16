from random import randint
li = []
for i in range(19):
    li.append(randint(10, 1000))
new_li = []
for li_items in li:
    if li_items % 2 == 0:
        li_items = max(li)
    new_li.append(li_items)
print(new_li)
