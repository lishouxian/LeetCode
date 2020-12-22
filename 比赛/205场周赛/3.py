import copy


class Solution:
    def minDays(self, grid) -> int:
        for p in range(len(grid)):
            for q in range(len(grid[0])):
                if 1 == grid[p][q]:
                    if self.isTwo(grid):
                        return 0
                    for i in range(len(grid)):
                        for j in range(len(grid[0])):
                            if grid[i][j] == 1:
                                grid[i][j] = 0
                                if self.isTwo(grid):
                                    return 1
                                grid[i][j] = 1

                    return 2
        return 0


    def isTwo(self, grid):
        grid2 = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.change(grid2,i,j)
                    for p in range(len(grid2)):
                        for q in range(len(grid2[0])):
                            if 1 == grid2[p][q]:
                                return True
                    break
        return False


    def change(self,grid2,i,j):
        grid2[i][j] = 0
        for p,q in [[-1,0],[1,0],[0,-1],[0,1]]:

            if 0 <= i+p < len(grid2) and 0 <= j+q < len(grid2[0]) and grid2[i+p][q+j] == 1:
                self.change(grid2, i+p, j+q)



a = Solution()
print(a.minDays([[1,1],[1,0]]))