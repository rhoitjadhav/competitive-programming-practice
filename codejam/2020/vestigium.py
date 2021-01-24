class Solution:
    def solve(self, *args):
        n = args[0]
        matrix = args[1]

        k = 0
        for i in range(n):
            k += matrix[i][i]

        r = 0
        for i in range(n):
            dup = set()
            for j in range(n):
                if matrix[i][j] in dup:
                    r += 1
                    break
                dup.add(matrix[i][j])
        
        c = 0
        for i in range(n):
            dup = set()
            for j in range(n):
                if matrix[j][i] in dup:
                    c += 1
                    break
                
                dup.add(matrix[j][i])

        return k, r, c

if __name__ == "__main__":
    sol = Solution()

    tests = int(input())
    
    for test in range(tests):
        n = int(input())
        matrix = [list(map(int, input().split())) for i in range(n)]
        result = sol.solve(n, matrix)
        
        print(f'Case #{test+1}: {result[0]} {result[1]} {result[2]}')
