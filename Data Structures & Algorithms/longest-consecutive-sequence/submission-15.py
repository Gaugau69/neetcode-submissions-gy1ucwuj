class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        cur_count = 1

        for i in s:

            if i-1 not in s:
                while i + 1 in s:
                    cur_count += 1
                    i += 1

            res = max(res, cur_count)
            cur_count = 1
        
        return res
                
