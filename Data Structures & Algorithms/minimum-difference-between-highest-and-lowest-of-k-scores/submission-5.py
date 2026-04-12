class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        n = len(nums)
        nums.sort()
        left, right = 0, k - 1
        cur_range = nums[right] - nums[left]
        min_range = cur_range

        for right in range(k, n):
            print(cur_range, min_range)

            left += 1
            cur_range = nums[right] - nums[left]
            min_range = min(min_range, cur_range)

        return min_range


