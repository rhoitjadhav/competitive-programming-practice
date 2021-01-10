# Forming a Magic Square

def formingMagicSquare(A):
    M = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    cost = map(lambda B: dist(A, B), M)
    return min(cost)


def dist(A, B):
    d = 0
    for i in range(3):
        for j in range(3):
            d += abs(A[i][j] - B[i][j])
    
    return d

if __name__ == "__main__":
    A = [[8, 1, 6], 
         [3, 5, 7], 
         [4, 9, 2]]
        
    print(formingMagicSquare(A))
