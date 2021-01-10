def knapsackLight(value1, weight1, value2, weight2, maxW):
    result = 0

    if value2 > value1:
        if weight2 <= maxW:
            result += value2
            maxW -= weight2

            if weight1 <= maxW:
                result += value1

        else:
            if weight1 <= maxW:
                result += value1

    else:
        if weight1 <= maxW:
            result += value1
            maxW -= weight1

            if weight2 <= maxW:
                result += value2
        else:
            if weight2 <= maxW:
                result += value2

    return result

v1 = 10
w1 = 5
v2 = 6 
w2 = 4
maxW = 9

result = knapsackLight(v1, w1, v2, w2, maxW)
print(result)
