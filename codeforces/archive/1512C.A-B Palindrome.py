class Solution:
    def is_palindrome(self, string):
        n = len(string)
        if n == 1:
            return "".join(string)

        for i in range(n//2):
            if string[i] != string[n-i-1]:
                return -1

        return "".join(string)

    def solve(self, a, b, string):
        n = len(string)

        for i in range(n):
            if string[i] == '?':
                string[i] = string[n-i-1]

        for i in range(n):
            if string[i] == '0':
                a -= 1
            if string[i] == '1':
                b -= 1

        for i in range(n//2):
            if string[i] == '?':
                if a > b:
                    string[i] = '0'
                    string[n-i-1] = '0'
                    a -= 2
                else:
                    string[i] = '1'
                    string[n-i-1] = '1'
                    b -= 2

        for i in range(n):
            if string[i] == '?':
                if a > b:
                    string[i] = '0'
                    string[n-i-1] = '0'
                    a -= 1
                else:
                    string[i] = '1'
                    string[n-i-1] = '1'
                    b -= 1

        if a == 0 and b == 0:
            return self.is_palindrome(string)

        return -1


if __name__ == '__main__':
    sol = Solution()
    tests = int(input())
    results = []
    for test in range(tests):
        a, b = tuple(map(int, input().split()))
        string = list(input())
        result = sol.solve(a, b, string)
        results.append(result)

    for result in results:
        print(result)
