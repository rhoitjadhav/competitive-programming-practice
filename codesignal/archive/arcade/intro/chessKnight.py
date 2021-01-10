def chessKnight(cell):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    x, y = d[cell[0]], int(cell[1])

    count = 0
    # x, y + 2
    if y + 2 < 9:
        if x - 1 > 0:
            count += 1
        if x + 1 < 9:
            count += 1

    # x, y - 2
    if y - 2 > 0:
        if x - 1 > 0:
            count += 1
        if x + 1 < 9:
            count += 1
    
    # x + 2, y
    if x + 2 < 9:
        if y - 1 > 0:
            count += 1
        if y + 1 < 9:
            count += 1

    # x - 2, y
    if x - 2 > 0:
        if y - 1 > 0:
            count += 1
        if y + 1 < 9:
            count += 1

    return count

cell = 'c2'
result = chessKnight(cell)

print(result)

