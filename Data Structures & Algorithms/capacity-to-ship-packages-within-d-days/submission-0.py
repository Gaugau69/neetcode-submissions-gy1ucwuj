class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        while left <= right:
            k = (left + right) // 2
            time = 1
            on = 0

            for x in weights:
                on += x
                if on > k:
                    time += 1
                    on = x
            
            if time <= days:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res


