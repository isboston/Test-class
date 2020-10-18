from random import randint

a_matrix = int(input('Enter the first number matrix:\n'))
b_matrix = int(input('Enter the last number matrix:\n'))
n_size_matrix = int(input('Enter n_size matrix:\n'))
m_size_matrix = int(input('Enter m_size matrix:\n'))
matrix = [[randint(a_matrix, b_matrix) for y in range(m_size_matrix)] for x in range(n_size_matrix)]
for i in range(n_size_matrix):
    for j in matrix[i]:
        print(j, end=' ')
    print()

# max element of matrix

max_elem = 0
for i in range(n_size_matrix):
    for j in range(m_size_matrix):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
print(f'max element of matrix: {max_elem}')

# min element of matrix

min_elem = matrix[0][0]
for i in range(n_size_matrix):
    for j in range(m_size_matrix):
        if matrix[i][j] < min_elem:
            min_elem = matrix[i][j]
print(f'min element of matrix: {min_elem}')

# sum elements of matrix

sum_elem = 0
for i in range(n_size_matrix):
    for j in range(m_size_matrix):
        sum_elem += matrix[i][j]
print(f'sum element of matrix: {sum_elem}')

# index max row

max_sum = 0
idx = -1
for i in range(n_size_matrix):
    sum_row = 0
    for j in range(m_size_matrix):
        sum_row += matrix[i][j]
        if sum_row > max_sum:
            max_sum = sum_row
            idx = i
print(f'index of max row: {idx}')

# index max column

max_sum = 0
idx = -1
for i in range(m_size_matrix):
    sum_col = 0
    for j in range(n_size_matrix):
        sum_col += matrix[j][i]
        if sum_col > max_sum:
            max_sum = sum_col
            idx = i
print(f'index of max column: {idx}')

# index min row

line_index_count = -1
min_sum = 0
min_line_index = 0
for line in matrix:
    for column in line:
        min_sum += column
    break
for index in matrix:
    line_sum = 0
    for elem in index:
        line_sum += elem
    line_index_count += 1
    if line_sum < min_sum:
        min_line_sum = line_sum
        min_line_index = line_index_count
print(f'index of min row: {min_line_index}')

# index min column

min_row = 0
column_summ = 0
while min_row < len(matrix):
    column = 0
    while column < len(matrix):
        column_summ += matrix[column][min_row]
        column += 1
    break
min_column_sum = column_summ
min_column_index = 0
min_column_count = -1
while min_row < len(matrix):
    column_sum = 0
    column = 0
    while column < len(matrix):
        column_sum += matrix[column][min_row]
        column += 1
    min_column_count += 1
    if min_column_sum > column_sum:
        min_column_sum = column_sum
        min_column_index = min_column_count
    min_row += 1

print(f'index of min column: {min_column_index}')
