# Breaking the Records

def breakingRecords(scores):
    high = scores[0]
    low = scores[0]

    h_count = 0
    l_count = 0

    for i in range(1, len(scores)):

        if scores[i] > high:
            # High
            high = scores[i]
            h_count += 1

        if scores[i] < low:
            # Low
            low = scores[i]
            l_count += 1

    return h_count, l_count

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result = breakingRecords(scores)

print(result)
