class Solution:
    def maxHeight(self, cuboids) -> int:

        temp = []
        for a in cuboids:
            a.sort()
            a.reverse()
            temp.append(a)
            # temp.append([a,b,c])
            # temp.append([a, c, b])
            # temp.append([b, a, c])
            # temp.append([b, c, a])
            # temp.append([c, a, b])
            # temp.append([c, b, a])

        temp = sorted(temp, key=lambda a:(a[0],a[1],a[2]))

        def inside(x,y):
            return temp[x][1] >= temp[y][1]  and temp[x][2] >= temp[y][2]
        ans = 0
        dp = [0] * len(temp)
        for i in range(len(temp)):
            dp[i] = temp[i][0]
            for j in range(i):
                if inside(i, j):
                    dp[i] = max(dp[i], dp[j] + temp[i][0])

            ans = max(ans, dp[i])

        return ans





a = Solution()
print(a.maxHeight([[29,59,36],[12,13,97],[49,86,43],[9,57,50],[97,19,10],[17,92,69],[92,36,15],[16,63,8],[94,24,78],[52,11,39],[48,61,57],[15,44,79],[6,69,98],[30,70,41],[23,17,33],[85,86,12],[13,75,98],[75,30,30],[89,18,27],[94,83,81]]))
