# Almost Increasing Sequence

# My Solution (Time Complexity is too large)
def almostIncreasingSequence(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if i == 0:
            if sequence[i] >= sequence[i + 1]:
                count += 1

        else:
            if sequence[i] >= sequence[i + 1]:
                count += 1
            
            if sequence[i - 1] == sequence[i + 1]:
                count += 1

    if count < 2:
        return True

    else:
        return False


# bandorthild's Solution
def almostIncreasingSequence(sequence):
    c = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]: c += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
    return c < 3
