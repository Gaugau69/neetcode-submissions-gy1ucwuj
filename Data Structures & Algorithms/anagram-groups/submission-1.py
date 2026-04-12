class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def IsAnagram(s:str) -> List:
            freq = [0] * 26

            for i in s:
                freq[ord(i) - ord("a")] += 1
            
            return freq
        
        ANAGRAMS = {}

        for word in strs:
            key = tuple(IsAnagram(word))

            if key in ANAGRAMS:
                ANAGRAMS[key].append(word)
            else:
                ANAGRAMS[key] = [word]
                
        return list(ANAGRAMS.values())


