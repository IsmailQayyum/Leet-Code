class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        minIndex = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[minIndex]:
                minIndex = i
            else:
                profit = max(profit,prices[i]-prices[minIndex])
        return profit
