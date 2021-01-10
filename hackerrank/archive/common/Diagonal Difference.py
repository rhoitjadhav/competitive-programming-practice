# Diagonal Difference

def diagonalDifference(arr):
    # Write your code here
    res1 = 0
    res2 = 0
    for i, array in enumerate(arr):
        # print(i, len(array) - 1 - i)

        dia_1 = array[i]
        dia_2 = len(array) - 1 - i

        res1 = res1 + dia_1
        res2 = res2 + array[dia_2]

    return (abs(res1 - res2))


arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

result = diagonalDifference(arr)
print(result)
