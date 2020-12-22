class Solution:
    def splitArray(self, nums):
        i = 0
        while i < len(nums)-2:
            if nums[i] == nums[i+1] == nums[i+2]:
                nums.pop(i)
            else: i= i+1

        def huzhi(a,b):
            if a == 1 or b == 1: return True
            if a == 0 or b == 0: return False
            else: 
                return huzhi(b, a%b)

        biaoji = [i for i in range(len(nums))]
        count = 1
        left = [0]

        while left:

            right = []
            for zimu in left:
                for i in range(len(biaoji)):

                    if not huzhi(nums[biaoji[i]],nums[zimu]):
                        if biaoji[i] == len(nums) - 1 :
                            return count
                        if (not biaoji[i] + 1 in right) and (not biaoji[i] + 1 in left) and biaoji[i+ 1] - biaoji[i] == 1:
                            right.append(biaoji[i+1])
            print(left)
            for zimu in left:
                biaoji.remove(zimu)
            print(biaoji)
            left = right
            count = count+1

a = Solution()
print(a.splitArray([2,2,3,3,2,3,4,5,2,56,2,3,7,19,31,97,101]))