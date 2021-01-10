class Solution:
    def solve(self, prices, k):
        min_price = min(prices)
        if k < min_price:
            return 0
        
        if k == min_price:
            return 1
        
        count = 0
        for p in sorted(prices):
            if k < p:
                break
            k -= p
            count += 1    
        
        return count