class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [[strs[0]]]

        if len(strs) == 1:
            return res

        for i in range(1, len(strs)):
            flag = False

            for j in res:
                if Counter(strs[i]) == Counter(j[0]):
                    j.append(strs[i])
                    flag = True
                    break
            
            if flag == False:
                res.append([strs[i]])
        
        return res
            

