# Search Insert Position
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1 
        
        return l


s = Solution()
n = [1, 3]
print(s.searchInsert(n, 4))
