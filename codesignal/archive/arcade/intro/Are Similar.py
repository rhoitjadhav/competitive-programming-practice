# Are Similar

def areSimilar(a, b):
    count = 0
    a1 = int
    a2 = int
    b1 = int 
    b2 = int
    n = len(a)

    for i in range(n):
        if a[i] == b[i]:
            continue

        count += 1

        if count > 2:
            return False

        if count == 1:
            a1 = a[i]
            b1 = b[i]

        if count == 2:
            a2 = a[i]
            b2 = b[i]
    
    if count == 0:
        return True
    elif (count == 2) and (a1 == b2 and b1 == a2):
        return True
    else:
        return False

# dnl-blkv's solution
from collections import Counter as C

def areSimilar1(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3


if __name__ == "__main__":
    a = [2, 1, 3]
    b = [1, 2, 3]

    print(areSimilar(a, b))
