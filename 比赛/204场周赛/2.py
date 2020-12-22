class Solution:
    def getMaxLen(self, nums):
        maxnum = 0
        start = -1
        left = -1
        right = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                left = -1
                right = 1
                start = i
            if nums[i] < 0:
                right = right * -1
                if left == -1:
                    left = i
                if right > 0:
                    maxnum = max(maxnum,i - start)
                else:
                    maxnum = max(maxnum, i - left)
            if nums[i] > 0:
                if right > 0:
                    maxnum = max(maxnum,i - start)
                else:
                    maxnum = max(maxnum,i - left)
        return maxnum

a = Solution()
print(a.getMaxLen([1,2,3,5,-6,4,0,10]))
print(a.getMaxLen([1,-2,-3,4]))


