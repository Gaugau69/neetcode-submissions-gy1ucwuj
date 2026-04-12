import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            time = 0

            for x in piles:
                time += math.ceil(x / k)
            
            if time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
                    
        return res
                 