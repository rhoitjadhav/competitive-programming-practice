class Solution:
    def solve(self, n, b):
        if n == 1: return '1'

        current = int(b[0]) + 1
        result = '1'

        for i in range(1, n):
            s = int(b[i]) + 1 
            if s == current:
                s = int(b[i]) + 0
                result += '0'
            else:
                result += '1'
            
            current = s

        return result


if __name__ == "__main__":
    s = Solution()

    tests = int(input())
    for i in range(tests):
        n = int(input())
        b = input()
        result = s.solve(n, b)
        print(result)
