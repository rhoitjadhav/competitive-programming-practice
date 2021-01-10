# Jumping on the Clouds: Revisited

def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    if k == n:
        if c[0] == 0:
            energy -= 1
        else:
            energy -= 3
        return energy

    i = k
    while True:
        if c[i] == 0:
            units = 1
        else:
            units = 3

        energy -= units
        if i == 0:
            break

        i += k
        if i >= n:
            i = i % n

    return energy


c = list(map(int, "1 1 0 1 0 1 0 1 0 1 0 1 1 0 1 1 1 1 1".split()))
k = 19

result = jumpingOnClouds(c, k)
print(result)
