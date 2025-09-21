class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i,v in enumerate(nums): ## goes through array and if the current value does not equal the count then return it -1
            if (i!=v):
                return v-1

            if v == len(nums)-1: # if its at the final node with no return then its a number you have to add 
                return v+1
     