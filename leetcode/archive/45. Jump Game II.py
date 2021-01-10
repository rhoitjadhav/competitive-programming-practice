from typing import List


class Solution:
    def jump_dynamic_programing(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 0 or n == 0:
            return 0
        
        jumps = [0 for i in range(n)]
        path = [0 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if i <= j + nums[j]:
                    jumps[i] += 1 + jumps[j]
                    path[i] = j
                    break
        

        print(path, jumps)
        return jumps[n-1]
    
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if nums[0] == 0 or n == 0:
            return 0
        
        jumps = 0
        i = 0
        count = 0
        count1 = 0
        while True:
            count += 1
            if i == n-1:
                break
            max_jump = -1
            start = i + 1
            end = start + nums[i]

            if end >= n:
                jumps += 1
                break
            
            count1 += end - start
            for j in range(start, end):
                next_jump = j + nums[j]
                if max_jump <= next_jump:
                    max_jump = next_jump
                    i = j

            jumps += 1 

        print(count, count1)
        return jumps
    
    def jump1(self, nums: List[int]) -> int:
        jumps, reach, max_reach = 0, 0, 0
        for i,num in enumerate(nums):
            if i > reach:
                reach = max_reach
                jumps += 1
            max_reach = max(max_reach, nums[i] + i)
        return jumps

if __name__ == "__main__":
    s = Solution()
    nums = [2,3,1,1,2,4,2,0,1,1]
    result = s.jump(nums)
    print(result)
