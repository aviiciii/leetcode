class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        d = dict(sorted(d.items(), key = lambda i: i[1], reverse= True))
        res = ""
        for ele in d:
            for j in range(d[ele]):
                res += ele
        return res

        