from functools import lru_cache


class Solution:
    def keyboard(self, k: int, n: int):
        help = [0] * 6
        help[0] = 26
        @lru_cache(None)
        def findx(a1,a2,a3,a4,a5,a6,nums):
            if nums == 0: return 1
            count = 0
            if a1 >0:
                count += a1  * findx(a1-1,a2+1,a3,a4,a5,a6,nums-1)
            if a2 > 0 and k >= 2:
                count += a2  * findx(a1, a2 - 1, a3+1, a4, a5, a6, nums - 1)
            if a3 > 0 and k >= 3:
                count += a3  * findx(a1, a2, a3-1, a4+1, a5, a6, nums - 1)
            if a4 > 0 and k >= 4:
                count += a4  * findx(a1, a2, a3, a4-1, a5+1, a6, nums - 1)
            if a5 > 0 and k >= 5:
                count += a5  * findx(a1, a2, a3, a4, a5-1, a6+1, nums - 1)
            return count % 1000000007
        return findx(26,0,0,0,0,0,n)



a = Solution()
print(a.keyboard(k = 1, n = 2))

