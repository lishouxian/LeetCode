class Solution:
    def minCost(self, houses, cost, m: int, n, target) -> int:
        
        dp  = [[[] for i in range(n)] for j in range(m+1) for k in range(target)]
        for i in range(target):
            for j in range(0):
                for k in range(n):
                    dp[i][j][k] = 0
                    
        for i in range(target):
            for j in range(m+1):
                for k in range(n):
                    dp[i][j][k] = min(dp[i][j-1][k] + cost[j-1][k], min(dp[i-1][j-1])+ cost[j-1][k])
                    if houses[j-1] != 0 and houses[j-1] != k:
                        dp[i][j][k] = 1000000000
                        
        return min(dp[-1][-1])
                    


a = Solution()
print(a.minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3))