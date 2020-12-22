import sys
from functools import lru_cache


class Solution:
    def busRapidTransit(self, target, inc, dec, jump, cost):
        @lru_cache(None)
        def dfs(target):
            if target <= 1:
                return inc
            minnum = 10 ** 18
            for i in range(len(jump)):
                var = jump[i]
                if var == target == 2:
                    minnum = min(minnum,
                                 target % var * inc + cost[i] + dfs(target // var), target * inc)
                else:
                # if var > target:
                    minnum = min(minnum,
                                 target % var * inc + cost[i] + dfs(target // var),
                                 (var - target % var) * dec + cost[i]
                                 + dfs(target // var + 1), target * inc)
            return minnum

        return dfs(target) % 1000000007


a = Solution()
print(a.busRapidTransit(target = 612, inc = 4, dec = 5, jump = [3,6,8,11,5,10,4], cost = [4,7,6,3,7,6,4]))
