class Solution:
    def minimumOperations(self, leaves: str) -> int:
        dp1 = [0 for i in range(len(leaves))]
        dp2 = [0 for i in range(len(leaves))]
        dp3 = [0 for i in range(len(leaves))]

        for i in range(len(leaves)):
            if leaves[i] == 'y':
                dp1[i] = dp1[i - 1] + 1
            else:
                dp1[i] = dp1[i - 1]

        dp2[0] = dp1[0]
        for i in range(1,len(leaves)):
            if leaves[i] == 'y':
                dp2[i] = min(dp2[i - 1], dp1[i-1])
            else:
                dp2[i] = min(dp2[i - 1] + 1,dp1[i -1] + 1)

        dp3[1] = dp2[1]
        for i in range(2,len(leaves)):
            if leaves[i] == 'y':
                dp3[i] = min(dp3[i - 1] + 1,dp2[i -1] + 1)
            else:
                dp3[i] = min(dp3[i - 1], dp2[i-1])

        return dp3[-1]


a = Solution()
print(a.minimumOperations("rrrrrr"))
