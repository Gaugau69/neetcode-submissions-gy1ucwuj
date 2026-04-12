class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        left = 0
        k = 0

        while left < len(nums):

            if nums[left] not in s:
                s.add(nums[left])
                k += 1
                nums[k - 1], nums[left] = nums[left], nums[k - 1]
                        
            left += 1

        return k