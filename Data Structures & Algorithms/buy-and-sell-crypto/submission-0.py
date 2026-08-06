class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suffmax = [0]*n
        suffmax[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            suffmax[i] = max(suffmax[i+1], prices[i])
        
        profits = []
        for i in range(n):
            profits.append(suffmax[i] - prices[i])
        
        return max(profits)