# Migratory Birds

def migratoryBirds(arr):
    max = 0
    bird_type = None

    birds_type = {
        5: 0,
        4: 0,
        3: 0,
        2: 0,
        1: 0
    }
    
    for i in arr:
        birds_type[i] += 1 

    for key, value in birds_type.items():
        if value >= max:
            max = value
            bird_type = key
    
    return bird_type

n = 6
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

result = migratoryBirds(arr)

print(result)
