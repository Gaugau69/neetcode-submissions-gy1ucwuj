class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for i in trust:
            graph[i[0]].append(i[1])

        s = set()
        
        for i in range(1, n + 1):
            if i not in graph.keys():
                s.add(i)   
        
        for key, val in graph.items():
            set_copy = s.copy()
            for j in set_copy:
                if j not in val:
                    s.remove(j)

        return next(iter(s)) if s else -1