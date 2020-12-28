class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        nums = [-1 for i in range (n+1)]
        nums[0] = 0
        nums[1] = 1
        for i in range(1,n+1):
            if 2 <= 2 * i <= n and nums[i] != -1:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 <= n and nums[i] != -1 and nums[i + 1] != -1:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)




a = Solution()
print(a.getMaximumGenerated(0))