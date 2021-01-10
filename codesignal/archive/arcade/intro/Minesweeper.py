def minesweeper(matrix):
    n = len(matrix)
    m = len(matrix[0])

    result = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            count = 0
            if i - 1 >= 0 and j + 1 != m and matrix[i - 1][j + 1]:
                count += 1
            if j + 1 != m and matrix[i][j + 1]:
                count += 1

            if i + 1 != n and j + 1 != m and matrix[i + 1][j + 1]:
                count += 1

            if i + 1 != n and matrix[i + 1][j]:
                count += 1

            if i + 1 != n and j - 1 >= 0 and matrix[i + 1][j - 1]:
                count += 1

            if j - 1 >= 0 and matrix[i][j - 1]:
                count += 1

            if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1]:
                count += 1

            if i - 1 >= 0 and matrix[i - 1][j]:
                count += 1

            result[i][j] = count

    return result


mat = [[False, False, False],
       [False, False, False],
       [False, False, False]]

result = minesweeper(mat)

for res in result:
    print(res)
