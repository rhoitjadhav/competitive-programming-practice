# Single Number
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}

        for num in nums:
            if map.get(num, False):
                map[num] += 1

            else:
                map[num] = 1

        for num in map:
            if map[num] == 1:
                return num

    # Using bit manupulation
    def singleNumber1(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


s = Solution()
nums = [2, 2, 1]
print(s.singleNumber(nums))
