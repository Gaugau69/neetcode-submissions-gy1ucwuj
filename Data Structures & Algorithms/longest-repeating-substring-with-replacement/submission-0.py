class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def most_frequent(s):
            freq = [0] * 26

            for i in s:
                freq[ord(i.lower()) - ord("a")] += 1
            
            max_letter = max(freq)

            return max_letter

        n = len(s)
        left = 0
        max_letter = 0

        for right in range(n):
            sub = s[left:right+1]
            rep = (right - left + 1) - most_frequent(sub)

            if rep > k:
                left += 1
            else:
                max_letter = max(max_letter, right - left + 1)
        
        return max_letter



