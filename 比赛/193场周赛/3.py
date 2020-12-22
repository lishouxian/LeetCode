class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        #nums = [4, 1, 5, 2, 9, 6, 8, 7]
        sorted_bloomDay = sorted(enumerate(bloomDay), key=lambda x: x[1])
        #idx = [i[0] for i in bloomDay]
        #nums = [i[1] for i in bloomDay]
        print(sorted_bloomDay)


a = Solution()
print(a.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))