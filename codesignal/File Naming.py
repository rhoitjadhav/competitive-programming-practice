def fileNaming(names):
    s = set()
    result = []
    for n in names:
        if n in s:
            i = 1
            name = f'{n}({i})'
            while True:
                if name in s:
                    i += 1
                    name = f'{n}({i})'
                else:
                    s.add(name)
                    result.append(name)
                    break

        else:
            s.add(n)
            result.append(n)

    return result


names = ["a(1)",
         "a(6)",
         "a",
         "a",
         "a",
         "a",
         "a",
         "a",
         "a",
         "a",
         "a",
         "a"]
result = fileNaming(names)

print(result)
