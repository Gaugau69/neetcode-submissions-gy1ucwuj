import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(min_heap, (dist, point))
        
        res = []
        for _ in range(k):
            x = heapq.heappop(min_heap)
            res.append(x[1])
        
        return res
