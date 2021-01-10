# Merge Sorted Array

from typing import List

class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            j = -(i + 1)
            a[j] = b[i]
        
        a.sort()
        return a
        

s = Solution()  
a = [0]
m = len(a)
b = [1]
n = len(b)
print(s.merge(a, m, b, n))
