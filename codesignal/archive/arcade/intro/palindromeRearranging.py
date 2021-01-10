# Palindrome Rearranging

def palindromeRearranging(string):
    d = dict()
    count = 0
    for s in string:
        d[s] = d.get(s, 0) + 1

    for key in d:
        if (d[key] % 2) != 0:
            count += 1
    
    return (count <=1)  

# andrew_pudge's solution
def palindromeRearranging1(inputString):

    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

if __name__ == "__main__":
    string = "aa"
    print(palindromeRearranging(string))