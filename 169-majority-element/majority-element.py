class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            try:
                d[i] += 1
            except:
                d[i] = 1

        maxi = max(d, key=lambda i:d[i])
        # maxi = max(d)

        return maxi