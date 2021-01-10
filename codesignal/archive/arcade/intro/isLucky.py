# Is Lucky
def isLucky(number):
    data = list(map(int,str(number)))
    n = len(data)
    sum1 = 0
    sum2 = 0
    for i in range(n//2):
        sum1 += data[i]
        sum2 += data[n - 1 - i]

    return sum1 == sum2


# andyman1337's solution
def isLucky1(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))


if __name__ == "__main__":
    print(isLucky(1230))