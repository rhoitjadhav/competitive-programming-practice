# Array Maximal Adjacent Difference

def arrayMaximalAdjacentDifference(a):
    output = 0
    for i in range(1, len(a)):
        output = max(abs(a[i-1] - a[i]), output)

    return output

# keeping_it_leal's solution
def arrayMaximalAdjacentDifference1(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)

if __name__ == "__main__":
    a = [2, 4, 1, 0]
    print(arrayMaximalAdjacentDifference(a))
