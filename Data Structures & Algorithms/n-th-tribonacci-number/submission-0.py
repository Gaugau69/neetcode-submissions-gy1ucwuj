class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def calcul(k):
            if k == 0:
                return 0
            elif k == 1:
                return 1
            elif k == 2:
                return 1
            elif k not in memo:
                memo[k] = calcul(k - 1) + calcul(k - 2) + calcul(k - 3)
            return memo[k]
        
        return calcul(n)