class Solution:
    def findDiagonalOrder(self, nums):
        count = []
        maxlens = 0
        save = 0
        for i in range(len(nums)):
            save += len(nums[i])
            maxlens = max(maxlens, i + len(nums[i]))

        count = [0] * save


        desave = 0
        for i in range(maxlens):
            a= i
            while a >= 0:
                b = i - a
                if len(nums) > a and len(nums[a]) > b:
                    count[desave] = nums[a][b]
                    desave += 1
                a = a - 1
        
        return count




a = Solution()
print(a.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))