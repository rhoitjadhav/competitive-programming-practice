# Adjecent Element Product

def adjacentElementProduct(inputArray):
    n = len(inputArray)
    max = inputArray[0] * inputArray[1]
    for i in range(1, n):
        if i + 1 == n:
            break
        product = inputArray[i] * inputArray[i + 1]

        if product > max:
            max = product

    return max
    

