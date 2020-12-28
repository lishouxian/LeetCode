class Solution:
    def maxProductPath(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dpfu = [[1] * (cols+1) for i in range(rows+1)]
        dpzheng = [[-1] * (cols+1) for i in range(rows+1)]


        for i in range(rows+1):
            for j in range(cols+1):
                if i == rows and j ==0:
                    dpfu[i][j] =1
                    dpzheng[i][j] = 1
                if i == 0 and j ==cols:
                    dpfu[i][j] =1
                    dpzheng[i][j] = 1
        for i in range(rows):
            for j in range(cols):
                a = min(dpfu[i-1][j],dpfu[i][j-1]) * grid[i][j]
                b = max(dpzheng[i - 1][j], dpzheng[i][j - 1]) * grid[i][j]
                if grid[i][j] >= 0:
                    dpfu[i][j] = a
                    dpzheng[i][j] = b
                else:
                    dpfu[i][j] = b
                    dpzheng[i][j] = a

        if dpzheng[-2][-2] < 0:
            return -1
        else:
            return dpzheng[-2][-2] % 1000000007

a = Solution()
print(a.maxProductPath(grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]))
