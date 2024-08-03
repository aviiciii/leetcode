class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for x in range(len(nums)):
            count = 0
            for i in range(len(nums)):
                ind= (i + x) % len(nums)
                if nums[i] == sorted_nums[ind]:
                    count += 1
            # print(count)
            if count == len(nums):
                return True
        return False