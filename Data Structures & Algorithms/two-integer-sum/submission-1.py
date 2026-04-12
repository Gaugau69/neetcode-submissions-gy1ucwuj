class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index:
                if i < index[complement]:
                    return [i, index[complement]]
                else:
                    return [index[complement], i]
            else:
                index[num] = i
        