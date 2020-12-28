from functools import lru_cache


class Solution:
    def stoneGameVII(self, stones):

        @lru_cache(None)
        def stonegame(left,right):
            if right - left <= 0:
                return 0
            elif right - left == 1:
                return max(stones[left:right + 1])
            else:
                return max(
                    min(stones[left + 1] + stonegame(left + 2,right),
                        stones[right] + stonegame(left + 1,right - 1)),
                    min(stones[left] + stonegame(left + 1, right - 1),
                        stones[right-1] + stonegame(left, right - 2))
                )


        return stonegame(0,len(stones)-1)





a = Solution()
print(a.stoneGameVII([5,3,1,4,2]))
