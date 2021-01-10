# Divisible Sum Pairs

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        j = i + 1
        while j < n:
            sum = (ar[i] + ar[j])
            if sum % k == 0:
                count += 1

            j += 1

    return count


k = 3
ar = [1, 3, 2, 6, 1, 2]
n = 6

result = divisibleSumPairs(n, k, ar)

print(result)
