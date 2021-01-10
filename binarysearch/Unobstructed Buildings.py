class Solution:
    def solve(self, heights):
        n = len(heights)

        if n == 0:
            return []

        if n == 1:
            return [0]

        maxx = float('-inf')
        new_heights = []

        for h in reversed(heights):
            maxx = max(maxx, h)
            new_heights.append(maxx)
        
        new_heights = list(reversed(new_heights))

        print(new_heights)
        result = []
        for i in range(n-1):
            if heights[i] > new_heights[i+1]:
                result.append(i)
        
        result.append(n-1)
        return result


s = Solution()
heights = [2,1,2]
result = s.solve(heights)
print(result)
