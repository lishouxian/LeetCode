class Solution:
    def minCount(self, coins) -> int:
        count = 0
        for coin in coins:
            count += (coin + 1) // 2
        return count



a = Solution()
print(a.minCount([2,3,10]))