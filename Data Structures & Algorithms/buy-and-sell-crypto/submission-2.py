class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 1
        max_profit = 0
        cur_profit = 0

        while right < n:
            if prices[right] > prices[left]:
                cur_profit = prices[right] - prices[left]
                max_profit = max(max_profit, cur_profit)

            else:
                left = right
            
            right += 1
        
        return max_profit