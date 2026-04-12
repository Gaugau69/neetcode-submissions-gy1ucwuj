class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(sol))
                return

            if openN < n:
                sol.append("(")
                backtrack(openN + 1, closedN)
                sol.pop()
            if closedN < openN:
                sol.append(")")
                backtrack(openN, closedN + 1)
                sol.pop()

        backtrack(0, 0)
        return res