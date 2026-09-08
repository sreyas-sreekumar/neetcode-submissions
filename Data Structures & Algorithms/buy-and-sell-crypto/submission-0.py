class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currentProfit = 0
        maxProfit = 0
        l = 0
        r = l+1
        for r in range(1,len(prices)):
            if prices[l] < prices[r]:
                currentProfit = prices[r]-prices[l]
            else: 
                l = r
            maxProfit = max(currentProfit,maxProfit)
        return maxProfit