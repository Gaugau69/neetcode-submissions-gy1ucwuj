class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        sett = set()
        left = 0
        max_size = -float("inf")

        for right in range(n):
            print(left, right)
            print(s[right])

            if s[right] not in sett:
                sett.add(s[right])
                max_size = max(max_size, right - left + 1)
            else:

                while s[right] in sett:
                    sett.remove(s[left])
                    left += 1
                
                sett.add(s[right])
            
        return max_size if max_size != -float("inf") else 0
            
