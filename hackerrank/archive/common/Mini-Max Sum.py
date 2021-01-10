# Mini-Max Sum

def miniMaxSum(arr):
    summ = sum(arr)
    minn = float('inf')
    maxx = float('-inf')

    for a in arr:
        diff = summ - a
        minn = min(minn, diff)
        maxx = max(maxx, diff)

    print(minn, maxx)


arr = [1, 3, 5, 7, 9]

miniMaxSum(arr)
