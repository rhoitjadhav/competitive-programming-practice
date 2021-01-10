# Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums) -> int:
        map = {}
        count = 0
        for i in nums:
            if map.get(i, False) is False:
                map[i] = True
                count += 1
        
        return count

    def removeDuplicates1(self, a: list()):
        if len(a) <= 1:
            return len(a)
        
        count = 1
        for i in range(len(a) - 1):
            if a[i] != a[i + 1]:
                a[count] = a[i + 1]
                count += 1
            
        print(a)
        return count

if __name__ == "__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))
    print(s.removeDuplicates1(nums))
