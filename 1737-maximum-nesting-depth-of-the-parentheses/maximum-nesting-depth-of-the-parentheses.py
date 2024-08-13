class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxi = 0
        for char in s:
            if char == '(':
                stack.append('(')
                if len(stack) > maxi:
                    maxi = len(stack)

            elif char == ')':
                if stack:
                    stack.pop()
        return maxi