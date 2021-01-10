def differentSymbolsNaive(string):
    diff = set()

    for s in string:
        diff.add(s)
        
    return len(diff)


s = "cabca"
result = differentSymbolsNaive(s)
print(result)