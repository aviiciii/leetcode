class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd=-1

        for i, ele in enumerate(num):
            if int(ele) % 2 != 0:
                odd = i
        print(odd)
        if odd != -1:
           
            return num[:odd+1]
        else:
            return str("")