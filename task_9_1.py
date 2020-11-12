li = ['first', 'second', 'third']
new_li = [f'{li_index + 1} - {li}' for li_index, li in enumerate(li)]
print(new_li)
