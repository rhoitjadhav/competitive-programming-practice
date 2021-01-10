# Sub-array Division

def birthday(s, d, m):
    count = 0
    end_point = len(s) - m + 1
    for i in range(len(s)):
        j = 0
        sum = 0

        if i == end_point:
            break

        while j < m:
            sum += s[i + j]
            j += 1

        if sum == d:
            count += 1

    return count


s = [1, 1, 1, 1, 1, 1]
d = 3
m = 2

result = birthday(s, d, m)

print(result)
