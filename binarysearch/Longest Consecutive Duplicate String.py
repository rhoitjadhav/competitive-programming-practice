class Solution:
    def solve(self, string):
        gcount = 0
        n = len(string)
        if n <= 1:
            return n
        
        ccount = 1
        for i in range(n-1):
            if string[i] == string[i+1]:
                ccount += 1
            else:
                gcount = max(gcount, ccount)
                ccount = 1
                
        return max(gcount, ccount)


s = Solution()
string = 'aabbb'
result = s.solve(string)
print(result)
