class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_sum = 0
        left = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            max_sum = max(max_sum, cur_sum)

            while cur_sum < 0 and left <= right:
                cur_sum -= nums[left]
                left += 1
        
        return max_sum