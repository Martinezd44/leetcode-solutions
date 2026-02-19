class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0] # this is the min value 
        best = 0 # best value
        for i in prices:
            if (min>i):
                min = i # iterate through to find the smallest value
            elif (i-min>best): # then after we check if the current value minus min is greater then the best for best profit
                best = i-min
        return best # we return the best profit if none it returns 0