class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        i = 1
        count = 0

        intervals.sort(key=lambda x: x[0])
        prev = intervals[0][1]

        while i < n:
            if intervals[i][0] < prev:
                count += 1
                prev = min(intervals[i][1], prev)
            else:
                prev = intervals[i][1]
            
            i += 1

        return count

