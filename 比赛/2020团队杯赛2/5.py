class Solution:
    def splitArray(self, nums):
        import collections
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
            print(left)
            right = []
            for zimu in left:
                if zimu == len(nums) - 1:
                    return count
                biaoji.remove(zimu)
                if not (zimu + 1 in right):
                    right.append(zimu+1)
                right.append(zimu + 1)
                for i in biaoji:
                    if not huzhi(nums[i],nums[zimu]):
                        if i == len(nums) - 1 :
                            return count
                        if not (i + 1 in right):
                            right.append(i+1)
            left = right
            count = count+1



a = Solution()
print(a.splitArray([2,2,3,3,2,3,4,5,2,56,2,3,7,19]))