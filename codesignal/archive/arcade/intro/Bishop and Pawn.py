def bishopAndPawn(bishop, pawn):
    d = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8}

    b = abs(int(d[bishop[0]]) - int(d[pawn[0]]))
    p = abs(int(bishop[1]) - int(pawn[1]))

    return b == p

    

b = "h1"
p = "a8"

81 
18

result = bishopAndPawn(b, p)

print(result)
