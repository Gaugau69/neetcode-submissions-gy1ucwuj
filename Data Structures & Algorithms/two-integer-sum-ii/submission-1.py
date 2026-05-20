class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dico = {}

        for i, num in enumerate(numbers):
            if target - num in dico:
                return [dico[target - num] + 1, i + 1]
            
            dico[num] = i
        