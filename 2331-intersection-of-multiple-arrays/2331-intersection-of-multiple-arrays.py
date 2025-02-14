class Solution(object):
    def intersection(self, nums):
        n = len(nums)
        c = Counter()
        
        for arr in nums:
            for i in arr:
                c[i] += 1
        
        result = []

        for i,j in c.items():
            if j==n:
                result.append(i)

        return sorted(result)