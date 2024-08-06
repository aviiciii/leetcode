class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = 0
        tot = 0
        

        for r in range(len(nums)):
            tot += nums[r]
            if tot < 1:
                tot = 0

            if tot > maxi:
                maxi = tot
        if maxi == 0:
            return max(nums)
        return maxi
    
