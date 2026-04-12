class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(nums):
            n = len(nums)

            if n == 2:
                return max(nums[0], nums[1])
            elif n == 1:
                return nums[0]
            elif n not in memo:
                memo[n] = max(dfs(nums[:-1]), dfs(nums[:-2]) + nums[-1])
            return memo[n]
        
        return dfs(nums)