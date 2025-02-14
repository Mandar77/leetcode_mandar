class Solution(object):
    def canChoose(self, groups, nums):
        i = 0  # Pointer for nums
        for group in groups:
            found = False
            while i <= len(nums) - len(group):  # Ensure enough elements left in nums for group
                if nums[i:i+len(group)] == group:
                    found = True
                    i += len(group)
                    break
                i += 1
            if not found:
                return False  # If group not found in nums or not enough elements left
        return True