class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, val in count.items():
            if val > n // 3:
                res.append(key)

        return res
