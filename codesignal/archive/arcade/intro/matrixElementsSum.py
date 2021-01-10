# Matrix Elements Sum

def matrixElementsSum(matrix):
    index = set()
    sum = 0
    n = len(matrix)
    for i in range(n):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                index.add(j)
            
            if not j in index:
                sum += matrix[i][j]

    return sum

if __name__ == "__main__":
    matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

    print(matrixElementsSum(matrix))


# keeping_it_leal's solution
def matrixElementsSum(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total
