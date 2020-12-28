class Solution:
    def constrainedSubsetSum(self, nums, k):

        count = [1] * len(nums)

        start = 0
        saved = 0
        minnums = 0
        countnums = 0

        for i in range(len(nums)):
            if nums[i] < 0 and start == 0:
                start = 1
                saved = i
                countnums += nums[i]

            elif nums[i] < 0:
                if i - saved < k:
                    countnums += nums[i]
                else:
                    countnums = countnums +  nums[i] - nums[i-k]
                    if minnums == 0:
                        minnums = countnums
                    else:
                        if countnums < minnums:
                            start = i - k
                            minnums = countnums
            elif i - saved < k:
                for j in range(start,i):
                    count[j] = 0

            else:
                for j in range(start, start + 1):
                    count[j] = 0

        newnums = []
        for i in range(len(nums)):
            if count[i]: newnums.append(nums[i])
        nums = newnums

        countnum = 0
        count = [1] * len(nums)
        start = 0
        for i in range(len(nums)-1):
            if countnum < 0:
                for j in range(start,i):
                    count[j] = 0

                start = i
                countnum = 0
            else:
                countnum += nums[i]

        newnums = []
        for i in range(len(nums)):
            if count[i]: newnums.append(nums[i])
        nums = newnums


        countnum = 0
        count = [1] * len(nums)
        start = i = len(nums) - 1
        while i > 0:
            if countnum < 0:
                star = i
                countnum = 0
            else:
                countnum += nums[i]
            i -= 1
        for j in range(start,len(nums)):
            count[j] = 0

        newnums = []
        for i in range(len(nums)):
            if count[i]: newnums.append(nums[i])
        nums = newnums

a = Solution()
print(a.constrainedSubsetSum([10,2,-10,5,20], 2))