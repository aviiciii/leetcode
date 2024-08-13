class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        indices = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
                indices.append(i)
                
            elif char == ')' and stack:
                if len(stack) == 1:
                    indices.append(i)
                else:
                    indices.pop()
                stack.pop()
        res = ''
        for i in range(len(s)):
            if i not in indices:
                res += s[i]

        return res