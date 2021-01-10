import math


def count_set_bits(number):
    count = 0

    if number != 0:
        for i in range(int(math.log2(number)), -1, -1):
            
            k = number >> i
            
            if k & 1:
                count += 1

    return count

test_case = int(input("Enter test case count: "))

for i in range(test_case):
    _n, _q = input("Enter no of students and query count: ").split()

    n = int(_n)
    q = int(_q)


    students = list(map(int, input("Enter students: ").strip().split()))[:n]

    p = list(map(int, input("Enter Query: ").strip().split()))[:q] 


    for query in p:
        even_count = 0
        
        for a in students:
            xor = query ^ a

            count = count_set_bits(xor)

            if count % 2 == 0:
                even_count += 1

        print("Test Case {} Query {}:".format(i+1, query), even_count, len(students)-even_count)


