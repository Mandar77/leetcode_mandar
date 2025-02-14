class Solution(object):
    def checkXMatrix(self, grid):
        n=len(grid)

        for i in range (n):
            for j in range (n):
                if i==j or i+j+1== n : 
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j]:
                    return False
        return True