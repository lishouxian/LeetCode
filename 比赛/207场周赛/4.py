class Solution:
    def connectTwoGroups(self, cost) -> int:
        rows = len(cost)
        cols = len(cost[0])

        dp = [[1000000] * (cols+1) for i in range(rows+1)]

        for i in range(rows):
            for j in range(cols):
                if i == j == 0:
                    dp[i][j] = cost[i][j]

                else:
                    minnum = 1000000
                    for p in range(i + 1):
                        minnum = min(minnum,cost[p][j])

                    dp[i][j] = min(
                        dp[i-1][j-1] + cost[i][j],
                        dp[i][j-1] + minnum,
                        dp[i-1][j] + min(cost[i][0:j+1])
                    )

        return dp[-2][-2]


a = Solution()
print(a.connectTwoGroups([[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))
