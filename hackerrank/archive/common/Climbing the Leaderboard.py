# Climbing the Leaderboard

def binary_search(arr, key, left, right):
    if key > arr[left]:
        return 1

    if key < arr[right]:
        return right + 2

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid + 1

        if arr[mid] > key and arr[mid + 1] < key:
            return mid + 2

        elif arr[mid] < key:
            right = mid - 1

        else:
            left = mid + 1

    return False


def climbingLeaderboard(scores, alice):
    output = list()
    unique_scores = [scores[0]]

    for i in range(1, len(scores)):
        if scores[i] != scores[i - 1]:
            unique_scores.append(scores[i])

    n = len(unique_scores)
    for a in alice:
        out = binary_search(unique_scores, a, 0, n - 1)
        output.append(out)

    return output


scores = list(map(int, "100 90 90 80 75 60".split()))
alice = list(map(int, "50 65 77 90 102".split()))
result = climbingLeaderboard(scores, alice)
print(result)
