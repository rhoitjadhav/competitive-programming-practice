string = "abca"
n = len(string)

for i in range(n//2):
    start = string[i]
    end = string[(n - 1) - i]

    if start != end:
        print(False)
        break

print(True)
