class Solution:
    def solve(self, nums, k):
        if len(nums) <= 1:
            return False
        hashset = set()

        for num in nums:
            if (k - num) in hashset:
                return True
            else:
                hashset.add(num)

        return False

sol = Solution()
nums = [1, 22]
k = 44
result = sol.solve(nums, k)
print(result)
