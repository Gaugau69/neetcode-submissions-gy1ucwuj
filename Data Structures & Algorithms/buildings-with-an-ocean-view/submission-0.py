class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxi = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxi and i not in res:
                maxi = heights[i]
                res.append(i)
                
        res.sort()

        return res