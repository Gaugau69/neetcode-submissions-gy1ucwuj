class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = []
        res = []

        for i in range(len(arr)):
            L.append((abs(x - arr[i]),i ))
        
        L.sort(key=lambda j: j[0])
        print(L)

        for i in range(k):
            res.append(arr[L[i][1]])
        
        res.sort()
        
        return res

