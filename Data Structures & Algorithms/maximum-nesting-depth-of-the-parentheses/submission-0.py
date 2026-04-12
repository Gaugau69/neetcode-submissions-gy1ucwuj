class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        count = 0

        for i in s:
            if i == '(':
                count += 1
            elif i == ')': 
                count -= 1
            
            maxi = max(maxi, count)

        return maxi
            