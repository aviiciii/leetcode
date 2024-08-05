class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        j = 0
        largest = 0
        while j < len(nums):
            if nums[j]!=1:
                if j-i > largest:
                    largest = j-i
                i = j+1
            j += 1
            print(largest)
        if j-i > largest:
            largest = j-i
        return largest