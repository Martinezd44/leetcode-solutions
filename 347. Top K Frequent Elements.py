class Solution(object):
    def topKFrequent(self, nums, k):
        count = {} #this is the count for hastable
        freq = [[]for i in range(len(nums) + 1)] #this is an array checks how often a value appears

        for num in nums:
            count[num] = 1 +count.get(num,0) # this keeps track of how many times it has occured and we store into a hashmap
        for num, cnt in count.items(): # this loops takes the count of how many times these values occurs stores it in freq
            freq[cnt].append(num)

        res = [] # result array we will be returning
        for i in range(len(freq)- 1,0,-1): # this loop takes the values stored in freq and appends it into result where we output
            for num in freq[i]:
                res.append(num)
                if len(res)==k: #this checks to see if we have the right amount of values in the output by checking with k
                    return res

       