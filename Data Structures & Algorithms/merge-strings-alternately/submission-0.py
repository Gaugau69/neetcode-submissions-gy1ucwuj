class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1) 
        m = len(word2) 
        l = 0
        r = 0
        word = []

        while l < n and r < m:
            word.append(word1[l])
            word.append(word2[r])
            l += 1
            r += 1
        
        if r == m:
            while l < n:
                word.append(word1[l])
                l += 1
        elif l == n:
            while r < m:
                word.append(word2[r])
                r += 1
        
        return "".join(word)

