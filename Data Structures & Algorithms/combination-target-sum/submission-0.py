class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(start, total):
            if total == target:
                res.append(sol[:])
                return
            
            if total > target:
                return
            
            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(i, total + nums[i])  
                sol.pop()
        
        backtrack(0, 0)
        return res

            
