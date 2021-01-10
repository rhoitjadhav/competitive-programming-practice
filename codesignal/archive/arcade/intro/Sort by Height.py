# Sort by Height

def sortByHeight(array):
    n = len(array)
    hash_set = set()
    copy_array = array.copy()

    # Remove -1 from array and Add index to hash set
    for i in range(n):
        if array[i] == -1:
            copy_array.remove(-1)
            hash_set.add(i)

    # Sort Array
    copy_array.sort()

    # Replace sorted elements from copy_array to original array 
    count = 0
    for i in range(n):
        if array[i] != -1:
            array[i] = copy_array[count]
            count += 1
    
    return array

# andrew_pudge's solution
def sortByHeight1(array):
    l = sorted([i for i in a if i > 0])

    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)

    return l

if __name__ == "__main__":
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(sortByHeight(a))
