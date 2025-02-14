class Solution(object):
    def maximumStrongPairXor(self, nums):
        arr=[]
        n=len(nums)
        for i in nums:
            for j in range (n):
                if abs(i-nums[j]) <= min(i,nums[j]):
                    arr.append(i^nums[j])
        
        return max(arr)