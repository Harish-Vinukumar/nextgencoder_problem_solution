# A Menu driven program which will accept
# two matrix of 3x3 and perform Arithmetic
# operations depending on user input
# Operations 1. Addition, 2. Subtraction, 3. Multiplication


import numpy as np


def addition(mat1, mat2):
    return mat1 + mat2

def subtraction(mat1, mat2):
    return mat1 - mat2

def multiplication(mat1, mat2):
    return mat1 * mat2


print("Provide values for the matrix1")
matrix1 = list()
for i in range(3):
    inner_list = list()
    for j in range(3):
        inner_list.append(int(input("Enter an element of matrix:\t")))
    matrix1.append(inner_list)

print("Provide values for the matrix2")
matrix2 = list()
for i in range(3):
    inner_list = list()
    for j in range(3):
        inner_list.append(int(input("Enter an element of matrix:\t")))
    matrix2.append(inner_list)
print("Matrix Operations: 1. Addition, 2. Subtraction, 3. Multiplication")

matrix1 = np.matrix(matrix1)
matrix2 = np.matrix(matrix2)
user_input = ""

while user_input != 0:
    user_input = int(input("Enter your choice:\t"))
    if user_input == 1:
        print("Addition of Matrix result:\n", addition(matrix1, matrix2))
    elif user_input == 2:
        print("Subtraction of Matrix result:\n", subtraction(matrix1, matrix2))
    elif user_input == 3:
        print("Multiplication of Matrix result:\n", multiplication(matrix1, matrix2))
    else:
        print("Kindly retry with available options!")