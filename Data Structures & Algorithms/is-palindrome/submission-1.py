class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = []
        for i in s:

            if i.isalnum():
                L.append(i.lower())
        
        s = "".join(L)

        left = 0
        right = len(s) - 1

        while left <= right:

            if s[left] != s[right]:
                return False
            
            else:
                left += 1
                right -= 1
        
        return True
            
