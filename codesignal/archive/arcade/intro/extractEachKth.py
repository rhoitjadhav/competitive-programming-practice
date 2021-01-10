from typing import List


def extractEachKth(a:List, k:int) -> List: 
    n = len(a)
    
    m = n // k

    remove_ele = []

    for i in range(1, m + 1):
        remove_ele.append(a[k * i - 1])
    
    for e in remove_ele:
        a.remove(e)

    return a

a = [1]
k = 2

result = extractEachKth(a, k)
print(result)
