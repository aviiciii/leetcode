class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for ele in nums:
            if abs(ele) == ele:
                positives.append(ele)
            else:
                negatives.append(ele)
        res=[]
        for i in range(len(positives)):
            res.append(positives[i])
            res.append(negatives[i])
        return res
            

