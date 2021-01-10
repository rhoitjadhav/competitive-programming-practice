# Move Zeroes

class Solution:
    def moveZeroes(self, a) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(a) <= 1:
            return None

        count = 0

        for i in range(len(a)):
            if a[i] == 0:
                count += 1
        
        for i in range(count):
            a.remove(0)
            a.append(0)
        
        print(a)

if __name__ == "__main__":
    s = Solution()
    a = [0,1,0,3,12]
    s.moveZeroes(a)