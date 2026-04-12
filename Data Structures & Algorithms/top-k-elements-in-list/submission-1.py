class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        ranking = [[] for i in range(len(nums) + 1)]


        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, occ in count.items():
            ranking[occ].append(num)
        
        for i in range(len(ranking) - 1, 0, -1):
            
            if ranking[i] != []:
                for num in ranking[i]:
                    res.append(num)
            
            if len(res) == k:
                return res
        
        return res





