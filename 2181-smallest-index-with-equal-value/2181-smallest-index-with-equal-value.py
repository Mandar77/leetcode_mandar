class Solution(object):
    def smallestEqual(self, nums):
        
        for i,n in enumerate(nums): 
            if i%10==nums[i]:
                return i
        return -1
        