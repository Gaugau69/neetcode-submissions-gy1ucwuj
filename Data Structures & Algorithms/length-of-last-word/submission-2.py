class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tot = 0
        flag = False

        for i in range(len(s) - 1, -1, -1):
            print(i)
            if s[i] == " " and flag == True:
                break
            if s[i].isalnum():
                flag = True
                tot += 1
            
        return tot