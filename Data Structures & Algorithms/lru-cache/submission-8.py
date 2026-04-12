class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recent = collections.deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.recent.remove(key)
        self.recent.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.recent.remove(key)
        elif len(self.cache) == self.capacity:
            lru = self.recent.popleft()
            del self.cache[lru]

        self.cache[key] = value
        self.recent.append(key)





