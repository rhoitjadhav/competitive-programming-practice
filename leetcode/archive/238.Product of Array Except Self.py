# Product of Array Except Self
import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return nums

        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[n-1] = 1
        for i in range(n-1):
            left[i+1] = nums[i] * left[i]

        for i in range(n-1, 0, -1):
            right[i-1] = nums[i] * right[i]

        return [left[i] * right[i] for i in range(n)]

    def productExceptSelf1(self, nums):
        n = len(nums)

        EPS = 1e-9
        summ = 0
        for i in range(n):
            summ += math.log10(nums[i])

        for i in range(n):
            nums[i] = int((EPS + math.pow(10.00, summ - math.log10(nums[i]))))

        return nums


s = Solution()
nums = [2, 3, 4]
print(s.productExceptSelf1(nums))
