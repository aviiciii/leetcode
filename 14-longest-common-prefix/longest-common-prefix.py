class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        length = len(min(strs))
        for i in range(length):

            count = 0
            letter=strs[0][i]

            for j in range(len(strs)):
                if strs[j][i] == letter:
                    count += 1
            if count == len(strs):
                pre += letter
            else:
                break
        return pre
            
