class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = []

        for i in s:
            if i.isalnum():
                L.append(i.lower())
        
        s_without_space = "".join(L)
        n = len(s_without_space)

        if n % 2 != 0:
            s_without_space = s_without_space[:n//2] + s_without_space[n//2 + 1:]
        
        middle = n // 2
        s_start = s_without_space[:middle]
        s_end = [i for i in s_without_space[middle:]]
        s_end_rev = s_end[::-1]
        s_end = "".join(s_end_rev)

        return s_start == s_end

