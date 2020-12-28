class Solution(object):
    def countVowelStrings(self, n):
        res = [[1 for i in range(5)] for i in range(51)]

        for i in range(1, 51):
            res[i][0] = res[i - 1][0]
            res[i][1] = res[i - 1][1] + res[i][0]
            res[i][2] = res[i - 1][2] + res[i][1]
            res[i][3] = res[i - 1][3] + res[i][2]
            res[i][4] = res[i - 1][4] + res[i][3]

        return sum(res[n-1])


a = Solution()
print(a.countVowelStrings(50))
