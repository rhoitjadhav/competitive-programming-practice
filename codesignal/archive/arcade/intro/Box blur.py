# Box blur

def boxBlur(image):
    n = len(image)
    m = len(image[0])
    output = list()
    ks = ls = 0
    ke = le = 3
    for i in range(n):
        if ke <= n:
            out = []
            for j in range(m):
                summ = 0
                if le <= m:
                    for k in range(ks, ke):
                        for l in range(ls, le):
                            summ += image[k][l]
                    out.append(summ // 9)
                    ls += 1
                    le += 1
            
            output.append(out)
            
            ls = 0
            le = 3
            ks += 1
            ke += 1

    return output

# keeping_it_leal' solution
def boxBlur1(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans

if __name__ == "__main__":
    image = [[7,4,0,1], 
             [5,6,2,2], 
            [6,10,7,8], 
             [1,4,2,0]]
    print(boxBlur(image))
    

