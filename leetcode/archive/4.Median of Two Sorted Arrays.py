# Median of Two Sorted Arrays
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1

        x = len(nums1)
        y = len(nums2)
        
        low = 0
        high = x
        
        while low <= high:
            partitionX = int((low + high) / 2)
            partitionY = int((x + y + 1) / 2 - partitionX)
            
            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float('-inf')
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float('-inf')
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxLeftX <= minRightY and minRightX >= maxLeftY:
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            # if not - move partitioning region
            elif maxLeftX > minRightY:
                high = partitionX -1
            else:
                low = partitionX + 1        


s = Solution()
nums1 = list(map(int, "1 2 3 4 5".split()))
nums2 = list(map(int, "6 7 8 9 10 11".split()))

print(s.findMedianSortedArrays(nums1, nums2))
