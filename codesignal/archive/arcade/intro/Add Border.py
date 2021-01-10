# Add Border

def addBorder(picture):
    n = len(picture)

    # Find max length of string in array
    str_max_len = len(picture[0])

    for i in range(n):
        if len(picture[i]) < str_max_len:
            req_star = (str_max_len + 2) - len(picture[i]) - 1
            picture[i] = "*" + picture[i] + (req_star * "*")  
            
        else:
           picture[i] = "*" + picture[i] + "*"

    # 0th and (n-1)th add `***`
    picture.insert(0, (str_max_len + 2) * "*")
    picture.append((str_max_len + 2) * "*")
    return picture

# simone_pgir's solution
def addBorder1(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]

if __name__ == "__main__":
    picture = ["abc", "dqed"]

    print(addBorder(picture))
