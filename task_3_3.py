new_line = input('Enter a line:\n')
if len(new_line) > 10:
    print(new_line + '!!!')
elif len(new_line) < 10:
    print(new_line[1])
