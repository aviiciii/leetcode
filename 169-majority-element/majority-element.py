class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums) / 2 
        for i in nums:
            try:
                d[i] += 1
                if d[i] > n:
                    return i
            except:
                d[i] = 1
            

        maxi = max(d, key=lambda i:d[i])
        # maxi = max(d)

        return maxi