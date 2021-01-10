# Are equally strong

def areEquallyStrong(a1, a2, b1, b2):
    sum1 = a1 + a2
    sum2 = b1 + b2

    if sum1 == sum2:
        max1 = max(a1, a2)
        max2 = max(b1, b2)

        return max1 == max2

    return False

# chris_l65's solution
def areEquallyStrong1(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}


if __name__ == "__main__":
    a1 = 20
    a2 = 15
    b1 = 5
    b2 = 20
    
    print(areEquallyStrong(a1, a2, b1, b2))

