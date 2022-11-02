def twoSum(nums: list[int], target: int) -> list[int]:


    for num in nums:
        if num>target:
            continue
        idx= nums.index(num)
        for next in nums[idx+1:]:
            if target == num+next:
                next_idx = nums[idx+1:].index(next)+len(nums[:idx+1])
                return [idx, next_idx]


    
    ans=0
    return ans


res=twoSum([3,2,3],6)
print(res)