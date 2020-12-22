class Solution:
    def shuffle(self, nums, n: int):
        res = [0 for i in range(2*n)]
        for i in range(2*n):
            if i%2 ==1:res[i] = nums[(i-1)//2+n]
            else:res[i] = nums[(i)//2]
        return res


a = Solution()
print(a.shuffle(nums = [2,5,1,3,4,7], n = 3))