#!/usr/bin/python3

def matrix_divided(matrix, div):
    """function to divide a matrix"""
    
    if not isinstance(matrix, list) or not matrix or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for l in matrix:
        if len(l) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not isinstance(l, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i in l:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")

        if not all(len(l) == len(matrix[0]) for l in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        n_matrix = [[round(i / div, 2) for i in j] for j in matrix]

        return n_matrix
