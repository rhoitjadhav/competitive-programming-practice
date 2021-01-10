# Counting Valleys

def countingValleys(n, s):
    count = int()
    valley_count = 0

    for i in s:
        if count == -1 and i == "U":
            valley_count += 1

        if i == "D":
            count -= 1

        if i == "U":
            count += 1

    return valley_count


n = 8
s = "UDDDUDUU"

result = countingValleys(n, s)

print(result)
