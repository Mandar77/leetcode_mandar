class Solution(object):
    def distributeCandies(self, candies, num_people):
        distribution = [0] * num_people
        give = 1
        idx = 0
        
        while candies > 0:
            distribution[idx % num_people] += min(candies, give)
            candies -= give
            give += 1
            idx += 1
        
        return distribution
        