# Sequence Equation

def permutationEquation(p):
    dct_keys = {}
    dct_values = {}
    output = []
    for i in range(len(p)):
        dct_keys[i+1] = p[i]
        dct_values[p[i]] = i + 1

    print(dct_keys, dct_values)

    for i in range(len(p)):
        x = dct_values[i + 1]
        y = dct_values[x]

        output.append(y)

    return output


p = list(map(int, "4".split()))
result = permutationEquation(p)
print(result)
