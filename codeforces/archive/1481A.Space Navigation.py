class Solution:
    def solve(self, px, py, string):
        if px == 0 and py == 0:
            return 'YES'

        n = len(string)
        s = [0, 0]
        for i in range(n):
            if string[i] == 'R':
                # x+1
                diff = abs(px - s[0])
                new = abs(px - (s[0] + 1))
                if new < diff:
                    s[0] += 1

            elif string[i] == 'L':
                # x-1
                diff = abs(px - s[0])
                new = abs(px - (s[0] - 1))
                if new < diff:
                    s[0] -= 1

            elif string[i] == 'U':
                # y+1
                diff = abs(py - s[1])
                new = abs(py - (s[1] + 1))
                if new < diff:
                    s[1] += 1

            else:
                # y-1
                diff = abs(py - s[1])
                new = abs(py - (s[1] - 1))
                if new < diff:
                    s[1] -= 1

        if s[0] == px and s[1] == py:
            return 'YES'

        return 'NO'


if __name__ == "__main__":
    s = Solution()

    tests = int(input())
    for i in range(tests):
        px, py = list(map(int, input().split()))
        string = input()
        result = s.solve(px, py, string)
        print(result)
