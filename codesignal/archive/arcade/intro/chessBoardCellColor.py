def chessBoardCellColor(cell1, cell2):
    dct = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}

    first = dct[cell1[0]]
    second = int(cell1[1])

    s1 = first + second

    first = dct[cell2[0]]
    second = int(cell2[1])

    s2 = first + second

    return (s1 % 2 == 0) == (s2 % 2 == 0) 

cell1 = 'A1'
cell2 = 'H3'

result = chessBoardCellColor(cell1, cell2)
print(result)
