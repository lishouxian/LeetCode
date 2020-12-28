class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxcandies = max(candies)
        back = [False] * len(candies)
        for i in range(len(candies)):
            if maxcandies - candies[i] <= extraCandies:
                back[i] = True
        return back


a = Solution()
print(a.kidsWithCandies([12,1,12],10))