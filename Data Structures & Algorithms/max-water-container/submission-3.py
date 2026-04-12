class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = -float("inf")

        while left < right:
            cur_vol = min(heights[left], heights[right]) * (right - left)
            max_vol = max(max_vol, cur_vol)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_vol
