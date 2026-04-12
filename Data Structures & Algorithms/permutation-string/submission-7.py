class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):        
            return False
        
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        for i in s1:
            freq_s1[ord(i) - ord("a")] += 1
        
        left = 0
        for right in range(len(s2)):
            print(freq_s2)
            freq_s2[ord(s2[right]) - ord("a")] += 1

            if s2[right] not in s1:
                left = right + 1
                freq_s2 = [0] * 26
                continue
            
            while freq_s2[ord(s2[right]) - ord("a")] > freq_s1[ord(s2[right]) - ord("a")]:
                freq_s2[ord(s2[left]) - ord("a")] -= 1
                left += 1

            if freq_s2 == freq_s1:
                return True

        return False

