"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        if n == 0:
            return True
            
        i = 1

        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end

        while i < n:
            if intervals[i].start < prev:
                return False
            else:
                prev = intervals[i].end
            
            i += 1
        
        return True