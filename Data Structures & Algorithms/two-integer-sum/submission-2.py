class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in indice:
                return [indice[complement], i]
            else:
                indice[num] = i
                