class Solution:
    def minStartValue(self, nums) -> int:
        minnum = 101
        save = 0
        for num in nums:
            save = save + num
            minnum = min(minnum,save)

        return max(1,1 - minnum )

a = Solution()
print(a.minStartValue([-3,2,-3,4,2]))


