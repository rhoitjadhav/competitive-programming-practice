class Solution:
    def solve(self, nums):
        odd = 0
        for num in nums:
            if num % 2 != 0:
                odd += 1
        
        if odd % 2 != 0:
            return -1
        
        return odd // 2

nums = [1, 1, 3, 7, 6, 12]
s = Solution()
result = s.solve(nums)
print(result)
