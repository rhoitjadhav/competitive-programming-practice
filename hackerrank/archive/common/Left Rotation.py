def reverse_array(start, end):
    n = (end - start) // 2
    for _ in range(n + 1):
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1 

def rotateLeft(d, a):
    n = len(a)
    if d > n:
        d = d % n

    d = n - d

    # part1
    part1 = n - d

    reverse_array(0, part1-1)

    # part2
    part2 = n - 1
    reverse_array(part1, part2)

    reverse_array(0, n - 1)
    return a

d = 14
a = list(map(int, "1 2 3 4 5".split()))

result = rotateLeft(d, a)
print(result)
