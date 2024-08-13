class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        start = goal[0]
        if start not in s:
            return False
            
        k = [i for i, j in enumerate(s) if j == start]
        


        for st in k:
            res = s[st:] + s[:st]
            print(res)
            if res == goal:
                return True
        return False