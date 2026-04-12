class MyHashMap:

    def __init__(self):
        self.bucket_size = 1000
        self.hashmap = [[] for _ in range(self.bucket_size)]        

    def put(self, key: int, value: int) -> None:
        bucket = self.hashmap[key % self.bucket_size]
        
        flag = False
        indice = None
        for i, (k, _) in enumerate(bucket):
            if k == key:
                indice = i
        
        if indice != None:
            bucket[indice] = (key, value)
        else:
            bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.hashmap[key % self.bucket_size]
        
        for i, (k, v) in enumerate(bucket):
                    if k == key:
                        return v
        
        return -1        

    def remove(self, key: int) -> None:
        bucket = self.hashmap[key % self.bucket_size]
        
        for i, (k, v) in enumerate(bucket):
                    if k == key:
                        bucket.pop(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)