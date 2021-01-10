# Between Two Sets

def gcd(n1, n2):
    while(n2):
        n1, n2 = n2, n1 % n2

    return n1


def lcm(n1, n2):
    return (n1 * n2) / gcd(n1, n2)


def getTotalX(arr1, arr2):
    lcm_ = 1
    for i in range(len(arr1)):
        lcm_ = lcm(lcm_, arr1[i])

    print("LCM:", lcm_)

    gcd_ = arr2[0]
    for i in range(1, len(arr2)):
        gcd_ = gcd(arr2[i], gcd_)

    print("GCD:", gcd_)

    i = 1
    result = lcm_
    count = 0
    while(result <= gcd_):
        result = lcm_ * i

        if gcd_ % result == 0:
            count += 1

        i += 1

    return count


a = list(map(int, "2 4".split()))
b = list(map(int, "16 32 96".split()))

result = getTotalX(a, b)
print(result)
