# Two Sum
class Solution:
    def twoSum(self, nums, target):
        hash_table = {}
        hash_table[nums[0]] = 0
        for i in range(1, len(nums)):
            print(i)
            key = target - nums[i]
            if key in hash_table:
                return [hash_table[key], i]
            else:
                hash_table[nums[i]] = i

        return []


s = Solution()
nums = [3, 2, 4]
target = 6

result = s.twoSum(nums, target)
print(result)
