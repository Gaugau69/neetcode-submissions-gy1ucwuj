class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        money_end = money - prices[0] - prices[1]
        return money_end if money_end >= 0 else money
