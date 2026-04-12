class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for inter in intervals:
            if inter[1] < newInterval[0]:
                res.append(inter)

        for inter in intervals:
            if inter[0] <= newInterval[0] <= inter[1]:
                newInterval[0] = inter[0]
            if inter[0] <= newInterval[1] <= inter[1]:
                newInterval[1] = inter[1]
        
        res.append(newInterval)

        for inter in intervals:
            if inter[0] > newInterval[1]:
                res.append(inter)

        return res
            
        

