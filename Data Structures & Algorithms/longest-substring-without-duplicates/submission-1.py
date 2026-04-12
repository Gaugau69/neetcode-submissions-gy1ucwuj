class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        longest = -float("inf")
        sett = set()

        for right in range(n):

            while s[right] in sett:
                sett.discard(s[left])
                left += 1
            
            cur = right - left + 1
            sett.add(s[right])
            longest = max(cur, longest)
        
        return 0 if longest == -float("inf") else longest
