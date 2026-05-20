class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}

        for i, num in enumerate(nums):
            if target - num in dico:
                return [dico[target - num], i]
            else:
                dico[num] = i