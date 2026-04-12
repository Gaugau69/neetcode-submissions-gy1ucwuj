class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            middle = (left + right) // 2
            print(middle)
            if nums [middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        
        if target > nums[middle]:
            return middle + 1
        else:
            return middle
        
        return middle