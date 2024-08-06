class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        ele = nums[0]

        for i in range(1,len(nums)):

            if count == 0:
                ele = nums[i]
                count = 1

            elif ele == nums[i]:

                count +=1
            else:

                count -=1
            if count > n/2:
                return ele

        return ele




        # d = {}
        # n = len(nums) / 2 
        # for i in nums:
        #     try:
        #         d[i] += 1
        #         if d[i] > n:
        #             return i
        #     except:
        #         d[i] = 1
            

        # maxi = max(d, key=lambda i:d[i])
        # # maxi = max(d)

        # return maxi

