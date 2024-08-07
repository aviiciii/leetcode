class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            sym = {
                ")": "(",
                "}":"{",
                "]":"["
            }
            if i in ["(", "{", "["]:
                stack.append(i)
            elif stack:
                if sym[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True
                