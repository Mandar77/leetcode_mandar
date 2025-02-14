class Solution(object):
    def passThePillow(self, n, time):
        time %= (n-1) * 2
        if time<n: 
            return time + 1
        return n - (time - (n-1))