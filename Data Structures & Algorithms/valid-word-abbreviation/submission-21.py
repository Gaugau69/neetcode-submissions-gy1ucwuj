class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0  # index word
        r = 0  # index abbr
        n = len(abbr)

        while r < n:
            if abbr[r].isdigit():
                if abbr[r] == '0':  # pas de nombre commençant par 0
                    return False
                num = 0
                while r < n and abbr[r].isdigit():
                    num = num * 10 + int(abbr[r])
                    r += 1
                l += num
            else:
                if l >= len(word) or abbr[r] != word[l]:
                    return False
                l += 1
                r += 1

        return l == len(word)
