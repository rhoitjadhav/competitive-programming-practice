# The Hurdle Race
def hurdleRace(k, height):
    maxx = max(height)
    if (maxx - k) < 0:
        return 0
    return maxx - k


height = list(map(int, "1 6 3 5 2".split()))
k = 4

result = hurdleRace(k, height)
print(result)
