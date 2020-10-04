line = input()
middle_of_line = int(len(line) // 2)
if line[middle_of_line] == line[0]:
    print(line[1:-1])
else:
    print(line[middle_of_line])
