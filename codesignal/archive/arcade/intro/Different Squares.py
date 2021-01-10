def differentSquares(matrix):
    n = len(matrix)
    m = len(matrix[0])

    if n < 2 or m < 2:
        return 0
    
    st = set()
    for i in range(n-1):
        for j in range(m-1):
            row = []
            for k in range(i, i + 2):
                col = []
                for l in range(j, j + 2):
                    col.append(matrix[k][l])
                row.append(tuple(col))
            st.add(tuple(row))
    
    return len(st)

matrix = [[3], 
 [4], 
 [5], 
 [6], 
 [7]]
result = differentSquares(matrix)
print(result)
