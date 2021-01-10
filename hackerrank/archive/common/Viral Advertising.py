# Viral Advertising
import math


def viralAdvertising(n):
    shared = 5
    liked = 2
    cummulative = 2
    for i in range(1, n):
        shared = liked * 3
        liked = math.floor(shared / 2)
        cummulative += liked

    return cummulative


n = 5
result = viralAdvertising(n)
print(result)
