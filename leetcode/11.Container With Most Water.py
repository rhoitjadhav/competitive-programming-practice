# Container With Most Water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = min(height)
        left = 0
        right = n-1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s.maxArea(height))
