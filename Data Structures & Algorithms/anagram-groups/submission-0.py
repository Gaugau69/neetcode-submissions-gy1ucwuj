class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def KeyAnagram(s:str) -> List:
            freq = [0] * 26

            for i in s:
                freq[ord(i) - ord("a")] += 1
            
            return freq
    
        ANAGRAMS = {}
        for word in strs:
            key = tuple(KeyAnagram(word))

            if key not in ANAGRAMS:
                ANAGRAMS[key] = [word]
            else:
                ANAGRAMS[key].append(word)
        
        return list(ANAGRAMS.values())





