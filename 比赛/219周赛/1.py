class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1 : return  0
        return self.numberOfMatches((n + 1) // 2) + n // 2


a = Solution()
print(a.getMaximumGenerated(0))