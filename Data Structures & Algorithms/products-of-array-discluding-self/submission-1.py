class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        count_0 = 0

        for i in nums:

            if i == 0:
                count_0 += 1
            
        if count_0 >= 2:
            return [0] * len(nums)
        
        elif count_0 == 1:
            prod = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    prod *= nums[i]
            
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(prod)
                else:
                    res.append(0)
        
        else:
            prod = 1
            for i in range(len(nums)):
                prod *= nums[i]
            
            for i in range(len(nums)):
                res.append(prod // nums[i])

        return res




