def lineEncoding(string:str):
    n = len(string)
    if n == 1: return string

    result = ""
    count = 1

    for i in range(1, n):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count == 1:
                result += string[i-1]
            else:
                result += str(count) + string[i-1]
                count = 1
    
    if count > 1:
        result += str(count) + string[-1]
    else:
        result += string[-1]

    return result

from itertools import groupby
def lineEncoding1(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x


string = "wwwwwwwawwwwwww"

result = lineEncoding(string)
print(result)
