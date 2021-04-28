class Solution:
    def longestPalindrome(self, string: str) -> str:
        n = len(string)

        if n < 2:
            return string

        gmax = 0
        for i in range(n):
            first = self.expand_from_middle(string, i, i)
            second = self.expand_from_middle(string, i, i+1)

            if gmax < first[0] or gmax < second[0]:
                if first[0] > second[0]:
                    gmax = first[0]
                    result = string[first[1]:first[2] + 1]

                else:
                    gmax = second[0]
                    result = string[second[1]:second[2] + 1]

        return result

    def expand_from_middle(self, string, left, right):
        n = len(string)
        while True:
            if left < 0 or right >= n:
                break

            if string[left] != string[right]:
                break

            left -= 1
            right += 1

        return right - left + 1, left+1, right-1


s = Solution()
string = 'abac'
result = s.longestPalindrome(string)
print(result)
