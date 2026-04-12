class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        overlap = [newInterval]
        interval_before = []
        interval_after = []

        for inter in intervals:
            if inter[1] < newInterval[0]:
                interval_before.append(inter)
            if inter[0] > newInterval[1]:
                interval_after.append(inter)
            if inter[0] <= newInterval[0] <= inter[1]:
                overlap.append(inter)
            if inter[0] <= newInterval[1] <= inter[1]:
                overlap.append(inter)
        
        mini = +float("inf")
        maxi = -float("inf")

        for inter in overlap:
            if inter[0] < mini:
                mini = inter[0]
            if inter[1] > maxi:
                maxi = inter[1]
        
        newInterval = [mini, maxi]

        return interval_before + [newInterval] + interval_after
            
        

