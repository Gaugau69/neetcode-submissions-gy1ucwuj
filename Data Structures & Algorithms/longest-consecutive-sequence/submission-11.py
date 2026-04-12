class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        res = 1
        cur_len = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cur_len += 1
            else:
                cur_len = 1
            res = max(res, cur_len)

        return res