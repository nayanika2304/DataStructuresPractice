'''
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to O.
'''

def setZeroes(A):
    m = len(A)  # number of rows, len of a column
    n = len(A[0])  # number of columns, len of a row
    zero_rows_indices = set()
    zero_cols_indices = set()
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                zero_rows_indices.add(i)
                zero_cols_indices.add(j)
    for i in range(m):
        if i in zero_rows_indices:
            A[i] = [0] * n
    for j in range(n):
        if j in zero_cols_indices:
            print(j)
            for cell in range(m):
                print(cell)
                A[cell][j] = 0
    return A

print(setZeroes(
    [
     [1,0,1],
     [1,1,1],
     [1,1,1]
    ]
))