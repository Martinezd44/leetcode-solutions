class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        duplicate = set(nums) #makes a set for no duplicates
        res = [] # result array we are returning
        for i in range(1, len(nums)+1): # we have to start at 1 since there is no 0 as a case
            if i not in duplicate: # checks if that value is in the array
                res.append(i) # if not we add it to result
        
        return res