class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0] * 26
        freq_t = [0] * 26

        for i in s:
            freq_s[ord(i) - ord("a")] += 1
        
        for j in t:
            freq_t[ord(j) - ord("a")] += 1
        
        return freq_s == freq_t