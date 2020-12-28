from functools import lru_cache


class Solution:
    def findBall(self, grid):
        m,n = len(grid), len(grid[0])
        res = []
        for i in range(n):
            x = i
            for j in range(m):
                if grid[j][x] == 1:
                    if x + 1 >= n or grid[j][x + 1] == -1:
                        x = -1
                        break
                    else:
                        x += 1
                else:
                    if x - 1 < 0 or grid[j][x - 1] == 1:
                        x = -1
                        break
                    else:
                        x -= 1

            res .append(x)
        return res








a = Solution()
print(a.findBall([[-1]]))
