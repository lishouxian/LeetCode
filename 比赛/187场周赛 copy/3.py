class Solution:
    def longestSubarray(self, nums, limit):
        left = right = 0
        maxnum = minnum = num[0]




        for i in range(1,len(num)):

            if nums[i] -minnum > limit:
                while 1:
                    if num[left] <num[i] -limit:
                        if 













a = Solution()
print(a.longestSubarray([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))