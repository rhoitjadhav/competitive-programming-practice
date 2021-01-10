# Cats and a Mouse

def catAndMouse(x, y, z):
    dist_A = abs(z - x)
    dist_B = abs(z - y)

    if dist_A < dist_B:
        return "Cat A"

    elif dist_A > dist_B:
        return "Cat B"

    else:
        return "Mouse C"


x = 1
y = 3
z = 2

result = catAndMouse(x, y, z)

print(result)
