class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
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

