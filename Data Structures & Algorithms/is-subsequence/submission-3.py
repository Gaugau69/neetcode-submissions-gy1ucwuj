class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n > m:
            return False
        
        if s == "":
            return True

        i = 0
        j = 0
        while i < m:
            if j == n:
                return True

            if t[i] == s[j]:
                j += 1

            print(i, j)
            
            i += 1
        
        if j == n:
            return True 
        
        return False

        
        