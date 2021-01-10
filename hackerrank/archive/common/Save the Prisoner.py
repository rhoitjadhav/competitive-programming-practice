# Save the Prisoner!

def saveThePrisonerBruteForce(n, m, s):
    for _ in range(m):
        m -= 1
        if m == 0:
            return s

        if s == n:
            s = 1
        else:
            s += 1

def saveThePrisoner(n, m, s):
    if m <= 1: return s
    if m < n: return s + (m - 1)
    
    return ((s + m - 2) % n) + 1
    

if __name__ == "__main__":
    # n, m, s = map(int, "94431605 679262176 5284458".split())

    with open("test.txt") as fp1, open("out.txt") as fp2:
        for x, y in zip(fp1, fp2):
            n, m, s = map(int, (x.strip()).split())
            y = int(y.strip())
            res = saveThePrisoner(n, m, s)

            print(y == res)


    # print(saveThePrisonerBruteForce(n, m, s), end=" ")
