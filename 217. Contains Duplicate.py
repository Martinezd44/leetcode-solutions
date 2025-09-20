class Solution(object):
    def containsDuplicate(self, nums):
        duplicate = set(nums)
        if (len(duplicate) == len(nums)):
            return False
        else:
            return True

            # this question is very easy since you can use a set which cannot contain duplicates and check if its the same length of nums if not then its True
      