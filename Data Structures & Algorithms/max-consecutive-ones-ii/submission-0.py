class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        max_sum = -float("inf")
        cur_sum = 0
        idx = None

        for right in range(n):

            if nums[right] == 1:
                cur_sum += 1
            elif nums[right] == 0 and idx == None:
                cur_sum += 1
                idx = right
            else:
                left = idx + 1
                cur_sum = 0
                idx = None
            
            max_sum = max(max_sum, cur_sum)
        
        return max_sum