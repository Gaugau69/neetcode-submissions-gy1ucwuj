class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []

        for i, num in enumerate(nums):
            
            prefix_idx = 0
            suffix_idx = len(nums)-1
            prod_pre = 1
            prod_suf = 1

            while prefix_idx < i:
                prod_pre *= nums[prefix_idx]
                prefix_idx += 1
            
            prefix.append(prod_pre)
            
            while suffix_idx > i:
                prod_suf *= nums[suffix_idx]
                suffix_idx -= 1

            suffix.append(prod_suf)

        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[i])

        return res



