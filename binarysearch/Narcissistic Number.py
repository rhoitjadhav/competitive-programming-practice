class Solution:
    def solve(self, n):
        if n < 9:
            return True
        
        digit_count = 0
        num = n
        while num != 0:
            num = num // 10
            digit_count += 1
        
        result = 0
        num = n
        while num != 0:
            rem = num % 10
            num = num // 10

            result += rem ** digit_count
        
        return result == n
