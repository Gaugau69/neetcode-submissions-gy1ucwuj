class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                res[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
            
            else:
                stack.append((temperatures[i], i))

        return res