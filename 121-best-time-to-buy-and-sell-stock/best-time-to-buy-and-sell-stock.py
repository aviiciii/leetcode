class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        greatest = 0
        while r<len(prices):
            dif = prices[r] - prices[l]
            if dif <= 0:
                l=r
            elif dif > greatest:
                greatest = dif
            
            r +=1
            print( greatest)
        return greatest