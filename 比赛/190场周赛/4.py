class Solution:
    def maxDotProduct(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        save = [[0] * l2 for _ in range(l1)]
        print(save)
        for i in range(l1):
            for j in range(l2):
                save[i][j] = nums1[i] * nums2[j]
        print(save)
        res = [[0] * (l2+1) for _ in range(l1+1)]
        for i in range(l1):
            for j in range(l2):
                res[i][j] = max(res[i-1][j-1],res[i-1][j-1]+save[i][j],save[i][j],res[i][j-1],res[i-1][j])
        print(res)
        maxnum = 0
        for i in range(l1):
            for j in range(l2):
                maxnum = max(maxnum,res[i][j])
        if maxnum > 0:return maxnum
        maxnum2 = - 1000000
        for i in range(l1):
            for j in range(l2):
                maxnum2 = max(maxnum2,save[i][j])
        return maxnum2






a = Solution()
print(a.maxDotProduct([5,-4,-3],[-4,-3,0,-4,2]))