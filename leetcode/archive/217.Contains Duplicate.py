# Contains Duplicate
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for num in nums:
            if num in freq:
                return True
            else:
                freq.add(num)

        return False


nums = [1, 2, 3]
s = Solution()
result = s.containsDuplicate(nums)
print(result)
