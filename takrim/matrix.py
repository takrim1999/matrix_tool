#!/usr/bin/python3


def trans(mat):
    new_mat = [[None for k in range(len(mat))] for l in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            new_mat[j][i] = mat[i][j]
    return new_mat

def process(mat):
    new_matrices = {}
    new_matrix = trans(mat)
    for i in range(len(new_matrix)-1):
        new_matrix.append(new_matrix[i])
    # print(new_matrix)
    for i in range(len(mat)):
        new_matrices[new_matrix[i][0]] = new_matrix[i+1][1:],new_matrix[i+2][1:]
    return new_matrices.items()    

def calc(data):
    return data[0]*((data[1][0][0]*data[1][1][1])-(data[1][1][0]*data[1][0][1]))
    # print(data[1][0][0])
def det(mat):
    sum = 0
    for i in process(mat):
            sum = sum + calc(i)
    return sum


order = int(input("order of your square matrix: "))
matrix = [[None for k in range(order)] for j in range(order)]
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
print("determinent is : " + str(det(matrix)))