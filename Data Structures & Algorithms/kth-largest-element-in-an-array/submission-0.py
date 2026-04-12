import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap) 

        for num in nums:
            heapq.heappush(max_heap, -num)
        
        for _ in range(k):
            x = heapq.heappop(max_heap)
        
        return -x
