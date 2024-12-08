string = input('Enter a few worlds:\n')
str_split = string.split()
result = " ".join(str_split[::-1])
print(result)
