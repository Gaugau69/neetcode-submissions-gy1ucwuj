class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for i in s:
            count_s[i] = count_s.get(i, 0) + 1

        for j in t:
            count_t[j] = count_t.get(j, 0) + 1

        if len(count_s.keys()) != len(count_t.keys()):
            return False

        for key, val in count_s.items():
            if key not in count_t or count_t[key] != val:
                return False
        
        return True
        
