class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort the numbers while keeping unique values
        sorted_nums = sorted(nums)
        # Map each number to its first index in the sorted list
        rank = {}
        for i, n in enumerate(sorted_nums):
            if n not in rank:
                rank[n] = i
        
        # Build the result: each number's rank = count of numbers smaller than it
        return [rank[n] for n in nums]