# Remove Element

class Solution:
    def removeElement(self, a, val: int) -> int:
        if len(a) <= 1:
            if val in a:
                a.remove(val)
                return 0
            else:
                return 1
        
        count = 0
        for i in range(len(a)):
            if a[i] == val:
                count += 1

        output = len(a) - count
        for i in range(count):
            a.remove(val)
        
        return output

if __name__ == "__main__":
    s = Solution()
    a = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(a, val))
