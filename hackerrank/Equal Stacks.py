from collections import deque


def equalStacks(h1: deque, h2: deque, h3: deque) -> int: 
    n = len(h1)
    m = len(h2)
    o = len(h3)
    dct = {
        'h1': sum(h1),
        'h2': sum(h2),
        'h3': sum(h3)
    }

        
    if dct['h1'] == dct['h2'] == dct['h3']:
        return dct['h1']

    while n or m or o:
        maxx = max(dct.values())

        for key in dct:
            if dct[key] == maxx:
                if key == 'h1':
                    dct[key] -= h1.popleft()
                    n -= 1
                elif key == 'h2':
                    dct[key] -= h2.popleft()
                    m -= 1
                else:
                    dct[key] -= h3.popleft()
                    o -= 1
                
                break
        
        if dct['h1'] == dct['h2'] == dct['h3']:
            return dct['h1']

    return 0

h1 = deque(map(int, "3 2 1 1 1".split()))
h2 = deque(map(int, "4 3 2".split()))
h3 = deque(map(int, "1 1 4 1".split()))


result = equalStacks(h1, h2, h3)
print(result)
