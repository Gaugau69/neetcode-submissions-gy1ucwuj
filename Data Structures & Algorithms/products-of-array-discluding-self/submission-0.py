class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        for i, num_i in enumerate(nums):
            product = 1

            for j, num_j in enumerate(nums):
                if j != i:
                    product *= num_j
            
            res.append(product)

        return res