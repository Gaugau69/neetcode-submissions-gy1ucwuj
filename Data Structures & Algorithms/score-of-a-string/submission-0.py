class Solution:
    def scoreOfString(self, s: str) -> int:
        tot = 0

        for i in range(len(s) - 1):
            tot += abs(ord(s[i + 1]) - ord(s[i]))
        
        return tot
