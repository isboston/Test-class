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

# 2) max element of matrix

max_elem = 0
for i in range(n_size_matrix):
    for j in range(m_size_matrix):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
print(f'max element of matrix: {max_elem}')

# 3) min element of matrix

min_elem = matrix[0][0]
for i in range(n_size_matrix):
    for j in range(m_size_matrix):
        if matrix[i][j] < min_elem:
            min_elem = matrix[i][j]
print(f'min element of matrix: {min_elem}')

# 4) sum elements of matrix

sum_elem = 0
for i in range(n_size_matrix):
    for j in range(m_size_matrix):
        sum_elem += matrix[i][j]
print(f'sum element of matrix: {sum_elem}')

# 5) index max row

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

# 6) index max column

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

# 7) index min row

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

# 8) index min column

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

# 9) reset all elements above the main diagonal

index_in_line = 0
while index_in_line < len(matrix):
    index_in_col = 0
    pos_of_main_diag = 0
    position_index = 0
    while index_in_col < len(matrix):
        pos_of_main_diag = index_in_line
        if index_in_line == index_in_col:
            position_index += 1
            index_in_col += 1
            continue
        if position_index > pos_of_main_diag:
            matrix[index_in_line][index_in_col] = 0
        position_index += 1
        index_in_col += 1
    index_in_line += 1
print('reset all elements above the main diagonal: ')
for i in matrix:
    print(i)

# 10) to zero all the elements below the main diagonal

index_in_line = 0
while index_in_line < len(matrix):
    index_in_col = 0
    pos_of_main_diag = 0
    position_index = 0
    while index_in_col < len(matrix):
        pos_of_main_diag = index_in_line
        if index_in_line == index_in_col:
            position_index += 1
            index_in_col += 1
            continue
        if position_index < pos_of_main_diag:
            matrix[index_in_line][index_in_col] = 0
        position_index += 1
        index_in_col += 1
    index_in_line += 1
print('to zero all the elements below the main diagonal: ')
for i in matrix:
    print(i)

# 11) two new matrix_a and matrix_b matrices of random numbers with dimension n*m

matrix_a = []
matrix_b = []
for col in range(n_size_matrix):
    matrix_line = []
    for line in range(m_size_matrix):
        matrix_line.append(randint(0, 9))
    matrix_a.append(matrix_line)
for col in range(n_size_matrix):
    matrix_line = []
    for line in range(m_size_matrix):
        matrix_line.append(randint(0, 9))
    matrix_b.append(matrix_line)
print('two new matrix_a and matrix_b matrices of random numbers with dimension n*m: ')
for i in matrix_a:
    print(i)
print()
for i in matrix_b:
    print(i)

# 12) matrix equal to the sum of matrix_a and matrix_b

matrix_a_plus_b = []
line = 0
while line < len(matrix_a):
    matrix_ab_line = []
    col = 0
    while col < len(matrix_a):
        elem_sum = matrix_a[line][col] + matrix_b[line][col]
        matrix_ab_line.append(elem_sum)
        col += 1
    matrix_a_plus_b.append(matrix_ab_line)
    line += 1
print('matrix equal to the sum of matrix_a and matrix_b: ')
for i in matrix_a_plus_b:
    print(i)

# 13) matrix equal to the difference between matrix_a and matrix_b

matrix_a_differ_b = []
line = 0
while line < len(matrix_a):
    matrix_ab_line = []
    col = 0
    while col < len(matrix_a):
        elem_diff = matrix_a[line][col] - matrix_b[line][col]
        matrix_ab_line.append(elem_diff)
        col += 1
    matrix_a_differ_b.append(matrix_ab_line)
    line += 1
print('matrix equal to the difference between matrix_a and matrix_b: ')
for i in matrix_a_differ_b:
    print(i)
