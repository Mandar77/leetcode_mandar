class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        n = len(nums)
        max_freq = 0
        left = 0
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]

            while (right - left + 1) * nums[right] - window_sum > k:
                window_sum -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq