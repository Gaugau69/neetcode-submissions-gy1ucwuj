class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = []

        for i in s:
            print(stack)
            if i.isdigit():
                num.append(i)
            elif i == '[':
                num = int(''.join(num))
                stack.append(num)
                num = []
            elif i == ']':
                sub_stack = []
                while type(stack[-1]) != int:
                    j = stack.pop()
                    sub_stack.append(j)
                sub_stack.reverse()
                pattern = ''.join(sub_stack)
                n = stack.pop()
                for _ in range(n):
                    stack.append(pattern)               
            else:
                stack.append(i)
        
        return ''.join(stack)
