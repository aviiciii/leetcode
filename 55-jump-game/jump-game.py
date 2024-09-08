class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #code here
        arr = nums
        cur = 0
        maxi = 0
	    
        while maxi < len(arr)-1:
            if cur > maxi:
                return False
	        
            # check cur arr
            if arr[cur]+cur > maxi:
                maxi = arr[cur]+cur
                
            cur +=1
        return True