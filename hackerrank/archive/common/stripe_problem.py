# Stripe Problem

# Using Binary conversion
import math
from datetime import datetime

max = 0
count = 0
result = ""

num = int(input("Enter number: "))

start = datetime.now().microsecond
for i in range(int(math.log2(num)), -1, -1):
    k = num >> i
    
    if (k & 1):
        count += 1

        if max < count:
            max = count
        
        result += "1"

    else:
        count = 0
        result += "0"

end = datetime.now().microsecond

print("Binary Conversion:", result)
print("Consecutinve Count:", max)
print("Time: {}".format(end-start))

# Using build in binary conversion using format() method

number = "{0:b}".format(int(input("Enter Number: ")))

print(number)

count = 0
max = 0

if number == "1":
    print(0)

else:
    for digit in number:
        if digit == "1":
            count += 1

            if max < count:
                max = count

        else:
            count = 0

print(max)
