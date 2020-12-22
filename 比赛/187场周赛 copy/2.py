class Solution:
    def kLengthApart(self, nums, k):
        left = 0
        for i in range(len(nums)):
            if left == 0:
                if nums[i] == 1:
                    left = i
            else:
                if nums[i] == 1:
                    if i - left <  k+1:
                        return False
                    left = i

        return True



            
a = Solution()
print(a.kLengthApart([0,0,0,0,1,0,1],1))