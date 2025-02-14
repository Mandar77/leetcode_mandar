class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i,j in enumerate(nums):
            if j>0: 
                break
            if i > 0 and j == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l<r:
                t_sum = j + nums[l] + nums[r]

                if t_sum < 0:
                    l +=1
                elif t_sum > 0:
                    r-= 1
                else: 
                    out.append([j,nums[l],nums[r]])
                    l+=1
                    r-=1
                    
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    
                    while nums[r] == nums[r+1] and l<r:
                        r-=1

        return out