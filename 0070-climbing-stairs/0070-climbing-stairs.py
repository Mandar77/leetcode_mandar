class Solution(object):
    def climbStairs(self, n):
            if n <= 2:
                return n
            
            # Initialize an array to store the number of ways to climb each step
            dp = [0] * (n + 1)
            dp[1] = 1  # One way to climb 1 step
            dp[2] = 2  # Two ways to climb 2 steps
            
            # Fill the array using the recurrence relation: dp[i] = dp[i-1] + dp[i-2]
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
            
            return dp[n]

        