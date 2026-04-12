class TimeMap:

    def __init__(self):
        self.timeMap  = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key] = self.timeMap.get(key, []) + [(value, timestamp)]        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        for i in self.timeMap[key]:
            if i[1] == timestamp:
                return i[0]

        for i in self.timeMap[key][::-1]:
            if i[1] <= timestamp:
                return i[0]

        return ""
        
