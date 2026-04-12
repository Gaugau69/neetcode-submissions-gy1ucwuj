class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        maxi = -float("inf")
        num_max = None

        for key, val in count.items():
            if val > maxi:
                num_max = key
                maxi = val
        
        return num_max