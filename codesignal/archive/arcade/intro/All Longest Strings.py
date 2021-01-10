# All Longest Strings

def allLongestStrings(inputArray):
    max = 0
    output_array = []

    for i in inputArray:
        if len(i) > max:
            max = len(i)
            output_array.clear()
            output_array.append(i)
            continue

        if len(i) == max:
            output_array.append(i)

    return output_array

if __name__ == "__main__":
    inputArray = ["abc", 
 "eeee", 
 "abcd", 
 "dcd"]

    print(allLongestStrings(inputArray))
