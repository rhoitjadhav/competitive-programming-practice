# Array Change

def arrayChange(a):
    cost = 0
    last_ele = a[0]
    for i in range(1, len(a)):
        if last_ele >= a[i]:
            last_ele += 1
            cost += abs(last_ele - a[i])
        else:
            last_ele = a[i]

    return cost

# bandorthild's solution
def arrayChange1(inputArray):
    a = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            a += f
    return a

if __name__ == "__main__":
    a = [-1000, 0, -2, 0]
    print(arrayChange(a))
