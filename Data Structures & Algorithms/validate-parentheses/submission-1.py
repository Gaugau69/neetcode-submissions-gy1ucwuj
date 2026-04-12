class Solution:
    def isValid(self, s: str) -> bool:
        L = []

        for i in s:
            
            if i == ')':
                if len(L) != 0 and L[-1] == '(':
                    L.pop()
                else:
                    return False
                           
            elif i == '}':
                if len(L) != 0 and L[-1] == '{':
                    L.pop()
                else:
                    return False

            elif i == ']':
                if len(L) != 0 and L[-1] == '[':
                    L.pop()
                else:
                    return False

            else:
                L.append(i)
        
        return True if len(L) == 0 else False


