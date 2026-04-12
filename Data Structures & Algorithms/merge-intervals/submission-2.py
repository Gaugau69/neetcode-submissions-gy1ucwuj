class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        i = 1

        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        while i < n:
            if res != [] and intervals[i][0] <= res[-1][1]:
                start = min(intervals[i][0], res[-1][0])
                end = max(intervals[i][1], res[-1][1])
                new_interval = [start, end]
                res[-1] = new_interval
            else:
                res.append(intervals[i])
            
            i += 1
        
        return res


