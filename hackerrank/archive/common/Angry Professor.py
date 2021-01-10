# Angry Professor

def angryProfessor(k, a):
    count = 0
    for i in a:
        if i < 1:
            count += 1

    if count >= k:
        return "NO"

    return "YES"


k = 3
a = list(map(int, "-1 -3 4 2".split()))

result = angryProfessor(k, a)
print(result)
