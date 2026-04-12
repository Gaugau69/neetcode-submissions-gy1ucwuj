class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def most_freq_charcahter(s:str) -> int:
            freq = [0] * 26

            for i in s:
                freq[ord(i.lower()) - ord("a")] += 1
            
            return max(freq)
        
        left = 0
        res = -float("inf")

        for right in range(1, len(s)):
            nb_turn = right - left  + 1 - most_freq_charcahter(s[left:right+1])
            if nb_turn > k:
                left += 1
            else:
                res = max(res, right - left + 1)
        
        return res
            




        