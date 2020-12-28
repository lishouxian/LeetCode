from functools import lru_cache


class Solution:
    def minimumEffortPath(self, heights):
        i=j=loss=res=0


        global loss,res
        res = 10 ** 9

        @lru_cache(None)
        def backtrack(i, j):
            global loss, res
            if i == len(heights) and j == len(heights):
                res = loss

            for a,b in [[0,1],[1,0],[0,-1],[-1,0]]:
                loss = max(loss, abs(heights[i][j] - heights[i+a][j+b]))

                backtrack(i + a, j + b)




            pass

        backtrack(i, j)



