class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(cost):
            n = len(cost)

            if n == 2:
                return min(cost[0], cost[1])
            elif n == 1:
                return 0
            elif n not in memo:
                memo[n] =  min(cost[0] + dfs(cost[1:]), cost[1] + dfs(cost[2:]))
            return memo[n]
        
        return dfs(cost)

            