class MedianFinder:

    def __init__(self):
        self.queue = []

    def addNum(self, num: int) -> None:
        l = 0
        r = len(self.queue) 

        while l < r:
            mid = (l + r) // 2
            if num >= self.queue[mid]:
                l = mid + 1
            else:
                r = mid 
        
        self.queue = self.queue[0:l] + [num] + self.queue[l:]

        return None

    def findMedian(self) -> float:
        n = len(self.queue)
        if n % 2 == 0:
            median = (self.queue[n // 2 - 1] + self.queue[n // 2])/2
            return median
        else:
            return self.queue[n // 2]
        
        