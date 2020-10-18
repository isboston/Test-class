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
