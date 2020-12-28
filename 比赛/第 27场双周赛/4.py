class Solution:
    def cherryPickup(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        res = [[0] * (cols) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res[i][j] = grid[i][j]

        dp = [[[0] * (cols+2) for i in range(cols+2)]for j in range(rows+1)]
        print(help)
        print(res)
        for k in range(1,rows+1):
            for i in range(1,cols+1):
                for j in range(1,cols+1):
                    maxnum = max(dp[k-1][i][j],dp[k-1][i+1][j],dp[k-1][i][j+1],dp[k-1][i-1][j],dp[k-1][i][j-1],dp[k-1][i+1][j+1],
dp[k-1][i-1][j-1],dp[k-1][i+1][j-1],dp[k-1][i-1][j+1]
                    )
                    if i == j:dp[k][i][j]= maxnum+res[k-1][i-1]
                    else:
                        dp[k][i][j] = maxnum+res[k-1][i-1]+ res[k-1][j-1]
                    
        back = 0
        for i in range(1,cols+1):
            for j in range(1,cols+1):
                back = max(back,dp[-1][i][j])
        print(dp)
        return back


   
a = Solution()
print(a.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))