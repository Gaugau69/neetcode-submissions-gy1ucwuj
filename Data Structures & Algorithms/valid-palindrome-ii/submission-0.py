class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r] and count == 2:
                return False
            elif s[l] != s[r] and count == 0:
                count += 1
                l += 1
            elif s[l] != s[r] and count == 1:
                count += 1
                l -= 1
                r -= 1
            else:
                l += 1
                r -= 1
        
        return True
