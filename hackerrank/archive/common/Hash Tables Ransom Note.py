# Hash Tables: Ransom Note
def checkMagazine(magazine, notes):
    magazine_dct = {}

    for m in magazine:
        if magazine_dct.get(m, False):
            magazine_dct[m] += 1

        else:
            magazine_dct[m] = 1
    
    for note in notes:
        if note in magazine_dct and magazine_dct[note] != 0:
            magazine_dct[note] -= 1
        else:
            return "No"
    
    return "Yes"


magazine = "two times three is not four".rstrip().split()

note = "two times two is four".rstrip().split()

print(checkMagazine(magazine, note))