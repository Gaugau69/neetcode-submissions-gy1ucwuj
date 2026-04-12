class TimeMap:

    def __init__(self):
        self.timeMap  = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key] = self.timeMap.get(key, []) + [(value, timestamp)]        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        left = 0
        right = len(self.timeMap[key]) - 1
        idx = None

        while left <= right:
            middle = (left + right) // 2

            if self.timeMap[key][middle][1] <= timestamp:
                idx = middle
                left = middle + 1
            
            else:
                right = middle - 1
        
        return self.timeMap[key][idx][0] if idx != None else ""

        
