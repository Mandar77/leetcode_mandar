class Solution(object):
    def removeTrailingZeros(self, num):
        nums = num [::-1]
        nums = nums.strip('0')
        return (nums [::-1])
        