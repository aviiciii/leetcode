class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) -1
        i = 0
        while i <= r:
            if nums[i] == 0:
                if i == l:
                    i +=1
                    l +=1
                    continue
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                # if i >= r:
                #     i=len(nums)
                #     continue
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i+= 1
            print(nums, i, l, r)
        print(nums)
