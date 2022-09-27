#!/usr/bin/python3


def trans(mat):
    new_mat = [[None for k in range(len(mat))] for l in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            # print(i,j,end='')
            # print(' to ',end='')
            # print(j,i,end='')
            # print('\n')
            new_mat[j][i] = mat[i][j]
    return new_mat

def det(mat):
    pass
    

order = int(input("order of your square matrix: "))
matrix = [[None for k in range(order)] for j in range(order)]
# print(len(matrix))
# matrix[0][0].append('hello')
# print(matrix)
for i in range(order):
    print('row ' + str(i+1) + " data:")
    for j in range(order):
        matrix[i][j] = (int(input('')))

print("your matrix is : ")

for col in matrix:
    print(col)
# print(matrix)
print("your transpose matrix is : ")

for col in trans(matrix):
    print(col)
# print(trans(matrix))