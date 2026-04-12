class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        m = len(s)
        
        if t == "":
            return 0

        i = 0
        j = 0
        while i < m:
            if j == n:
                return 0

            if s[i] == t[j]:
                j += 1
            
            i += 1

        return n - j        
        