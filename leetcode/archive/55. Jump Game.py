from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return True

        if nums[0] == 0 and n > 1:
            return False

        reachable = 0
        for i in range(n-1):
            if i > reachable:
                return False
            reachable = max(i + nums[i], reachable)

        return reachable >= n-1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 0]
    result = s.canJump(nums)
    print(result)
