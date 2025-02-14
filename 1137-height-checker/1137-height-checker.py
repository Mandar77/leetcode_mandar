class Solution(object):
    def heightChecker(self, heights):
        s_height=[]
        for q in heights:
            s_height.append(q)
        s_height.sort()
        print(s_height)
        print(heights)
        unmatch = 0
        start = 0
        limit = len(heights) - 1
        while start <= limit:
            if heights[start] != s_height[start]:
                unmatch += 1
            start += 1
        return unmatch
        