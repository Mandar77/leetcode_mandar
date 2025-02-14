class Solution(object):
    def differenceOfSum(self, nums):
        y=0
        x=sum(nums)        
        for i in nums:
            while i:
                y=y+i%10
                i=i//10
        return abs(x-y)