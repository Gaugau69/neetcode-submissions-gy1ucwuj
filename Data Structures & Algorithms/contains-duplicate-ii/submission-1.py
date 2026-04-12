class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        VISITED = {}

        for i in range(n):

            if nums[i] in VISITED:
                
                if abs(VISITED[nums[i]] - i) <= k:
                    return True
                else:
                    VISITED[nums[i]] = i
            
            else:
                VISITED[nums[i]] = i
        
        return False