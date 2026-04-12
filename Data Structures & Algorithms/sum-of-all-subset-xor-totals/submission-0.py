class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)        
        tot = 0

        for l in res:
            result = 0
            for i in l:
                result ^= i

            tot += result 

        return tot