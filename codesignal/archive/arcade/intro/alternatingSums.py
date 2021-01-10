# Alternating sums

def alternatingSums(a):
    n = len(a)
    first_team = 0
    second_team = 0

    for i in range(0, n, 2):
        first_team += a[i]
        if i+1 < n:
            second_team += a[i+1]

    return [first_team, second_team]

# andrew_pudge's solution
def alternatingSums1(a):
    return [sum(a[::2]),sum(a[1::2])]

if __name__ == "__main__":
    a = [50, 60, 60, 45, 70]
    print(alternatingSums(a))
