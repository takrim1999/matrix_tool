#!/usr/bin/python3

def trans(mat):
    new_mat = [[None for k in range(len(mat))] for l in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            new_mat[j][i] = mat[i][j]
    return new_mat

def process(mat):
    new_matrices = []
    new_matrix = trans(mat)
    for i in range(len(new_matrix)-1):
        new_matrix.append(new_matrix[i])
    # print(new_matrix)
    for i in range(len(mat)):
        new_matrices.append(new_matrix[i][0])
        for j in range(1,len(mat)):
            # if new_matrix[i][0] in new_matrices:
            new_matrices.append(new_matrix[i+j][1:])
            # else:
            #     new_matrices[new_matrix[i][0]] = list(new_matrix[j][1:])
    print(new_matrices)
    # return new_matrices.items()    

# def calc(lists):
#     lists[]

# def calc(data):
#     return data[0]*((data[1][0][0]*data[1][1][1])-(data[1][1][0]*data[1][0][1]))
#     # print(data[1][0][0])

# def det(mat):
#     # pass
#     sum = 0
#     for i in process(mat):
#             sum = sum + calc(i)
#     return sum


order = int(input("order of your square matrix: "))
matrix = [[None for k in range(order)] for j in range(order)]
for i in range(order):
    print('row ' + str(i+1) + " data:")
    for j in range(order):
        matrix[i][j] = (int(input('')))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("your matrix is : ")

for col in matrix:
    print(col)
# print(matrix)
print("your transpose matrix is : ")

for col in trans(matrix):
    print(col)
# print("determinent is : " + str(det(matrix)))
process(matrix)