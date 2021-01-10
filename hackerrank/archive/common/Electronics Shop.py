# Electronics Shop

def getMoneySpent(keyboards, drives, b):
    result = -1
    for k in keyboards:
        for d in drives:
            sum = k + d
            if sum <= b and result < sum:
                result = sum

    return result

if __name__ == "__main__":
    
    keyboards = [4]
    drives = [5]
    b = 5

    result = getMoneySpent(keyboards, drives, b)

    print(result)
