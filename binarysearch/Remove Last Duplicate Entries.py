class Solution:
    def solve1(self, nums):
        indices = {}
        for i, n in enumerate(nums):
            if indices.get(n):
                indices[n] += 1
            else:
                indices[n] = 1

        indices = {key:indices[key] for key in indices if indices[key] > 1}
        result = []

        for n in nums:
            count = indices.get(n)
            if count is None:
                result.append(n)
            elif count > 1:
                result.append(n)
                indices[n] -= 1
            else:
                pass
        return result

    def solve(self, nums):
        duplicates = {}

        for num in nums:
            if duplicates.get(num):
                duplicates[num] += 1
            else:
                duplicates[num] = 1
        
        result = []
        for num in reversed(nums):
            if duplicates[num] > 1:
                duplicates[num] = 1
            else:
                result.append(num)
        
        result.reverse()

        return result

s = Solution()  
nums = [3, 3, 0, 3, 3, 0, 1]
result = s.solve(nums)
print(result)
