
from functools import lru_cache

matrix = [[-37,-50,-3,44],[-37,46,13,-32],[47,-42,-3,-40],[-17,-22,-39,24]]
res = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

@lru_cache(None)
def backtrack(i,j):
    leftnum = 1000000000
    leftj = j
    for k in range(len(matrix[0])):
        if 0< matrix[i][j] - matrix[i][k] < leftnum:
            leftnum = matrix[i][j] - matrix[i][k]
            leftj = k
    rightnum = 1000000000
    righti = i
    for k in range(len(matrix)):
        if 0 < matrix[i][j] - matrix[k][j] < rightnum:
            rightnum = matrix[i][j] - matrix[k][j]
            righti = k

    if leftj == j and righti == i :
        res[i][j] = 1
        return 1
    else:
        if leftj == j:
            res[i][j] = backtrack(righti,j) +1
        elif righti == i:
            res[i][j] = backtrack(i, leftj) + 1
        else:
            res[i][j] = max(backtrack(i,leftj),backtrack(righti,j)) +1
        return res[i][j]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        backtrack(i,j)

for i in range(len(matrix)):
    minnum = 0
    for j in range(len(matrix[0])):
        if matrix[i][j] == min(matrix[i]):
            minnum = max(minnum,res[i][j])



print(res)