def avoidObstacles0(a):
    d = 2

    while True:
        flag = False
        for i in range(len(a)):
            if (a[i] % d) == 0:
                d += 1
                flag = True
                break
        
        if flag is False:
            return d

# andrew_pudge's solution
def avoidObstacles1(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1

# hrithik_sql's solution
def avoidObstacles2(inputArray):
    i=2
    while True:
        if all(x%i!=0 for x in inputArray):
            return i
        i=i+1

def avoidObstacles(a):
    d = 2

    i = 0
    while (i < len(a)):
        if (a[i] % d) == 0:
            d += 1
            flag = True
            i = 0
            continue
        
        i += 1

    # for i in range(len(a)):
    #     if (a[i] % d) == 0:
    #         d += 1
    #         flag = True
    #         i = -1

    return d

if __name__ == "__main__":
    a = [1000, 999]
    print(avoidObstacles(a))

