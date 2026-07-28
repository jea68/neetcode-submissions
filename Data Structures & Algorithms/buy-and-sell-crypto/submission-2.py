class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # sliding window way
        l = 0
        r = 0
        prevMin = float("inf")
        res = 0

        while r < len(prices):
            
            res = max(res, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return res
        
        
        # brute force ish way
        l = 0
        prevMin = float("inf")
        res = 0
        for i in range(len(prices)):
            if prices[i] >= prevMin:
                continue
            prevMin = prices[i]

            for j in range(i+1, len(prices)):

                res = max(res, prices[j] - prices[i])
        
        return res

