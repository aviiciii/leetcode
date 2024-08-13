class Solution:
    def myAtoi(self, s: str) -> int:
        # clean 
        s= s.lstrip()
        sign = 1

        # read sign
        if s and s[0]== '-':
            sign = -1
            s=s[1:]
        elif s and s[0] == '+':

            s = s[1:]
        
        print(s)
        index = 0


        # read int
        for i in range(len(s)):
            if not s[i].isdigit():
                index = i
                break
            index = len(s)
        n = s[:index]

        if n:
            n = int(n) * sign
            if (n > (2**31)-1):
                n = (2**31) -1
               
                # print("if")
            elif (n < -(2 ** 31)):
                n = -(2 ** 31)
                # print("else")
            return n

        return 0
