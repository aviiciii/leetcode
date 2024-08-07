class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sym = {
            ")": "(",
            "}":"{",
            "]":"["
        }

        for i in s:
            
            if i in sym.values():
                stack.append(i)
            elif stack:
                if sym[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False


        return not stack


                