class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res, sol = [], []
        dico = {'2':['A', 'B', 'C'], '3':['D', 'E', 'F'], '4':['G', 'H', 'I'], '5':['J', 'K', 'L'], '6':['M', 'N', 'O'], '7':['P', 'Q', 'R', 'S'], '8':['T', 'U', 'V'], '9':['W', 'X', 'Y', 'Z']}

        def backtrack(start):
            if start == len(digits):
                res.append("".join(sol))
                return

            for char in dico[digits[start]]:
                sol.append(char.lower())
                backtrack(start + 1)
                sol.pop()

        backtrack(0)
        return res