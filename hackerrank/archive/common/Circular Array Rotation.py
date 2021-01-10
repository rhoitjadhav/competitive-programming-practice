# Circular Array Rotation

def reverse_array(start, end):
    n = (end - start) // 2
    for i in range(n + 1):
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1 


def circularArrayRotation(a, k, queries):
    n = len(a)
    
    if n == k or k % n == 0:
        print(a)
        return [a[q] for q in queries]

    if k > n:
        part1 = n - (k % n)
    else:
        part1 = n - k
    
    part2 = n

    # Reverse part1
    reverse_array(0, part1 - 1)
    
    # Reverse part2
    reverse_array(part1, n - 1)

    # Reverse part1 + part2
    reverse_array(0, n - 1)

    return [a[q] for q in queries]

a = list(map(int, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15".split()))
k = 11
queries = list(map(int, "0 1 2".split()))

result = circularArrayRotation(a, k, queries)
print(result)