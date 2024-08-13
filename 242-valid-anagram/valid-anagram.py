import itertools

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        for char in s:
            if char in count_s.keys():
                count_s[char] +=1
            else:
                count_s[char] = 1
        

        count_t={}
        for char in t:
            if char in count_t.keys():
                count_t[char] +=1
            else:
                count_t[char] = 1

        if count_s == count_t:
            return True
        return False