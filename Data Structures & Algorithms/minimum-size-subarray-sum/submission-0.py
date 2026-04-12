class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini_size = float("inf")
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            print(cur_sum)
                        
            while cur_sum >= target:
                mini_size = min(mini_size, right - left + 1)
                cur_sum -= nums[left]
                left += 1
  
        return mini_size if mini_size != float("inf") else 0