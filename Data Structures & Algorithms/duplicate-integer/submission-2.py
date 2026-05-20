class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L = list(set(nums))

        if len(L) < len(nums):
            return True
        else:
            return False