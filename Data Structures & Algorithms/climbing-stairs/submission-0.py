class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(k):
            if k <= 2:
                return k
            elif k not in memo:
                memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]
        
        return dfs(n)