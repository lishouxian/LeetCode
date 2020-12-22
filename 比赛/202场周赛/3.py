class Solution:
    def maxSum(self, nums1, nums2):
        save1 = [0]* (len(nums1) + 1)
        save2 = [0]* (len(nums2) + 1)
        # save1[len(nums1)] = 0
        # save2[len(nums2)] = 0
        for i in range(-1,len(nums1)-1):
            save1[i+1] = save1[i] + nums1[i+1]
        for i in range(-1,len(nums2)-1):
            save2[i+1] = save2[i] + nums2[i+1]

        print(save1,save2)
        last1 = last2 = -1
        count = 0
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                count += max(save1[i] - save1[last1], save2[j] - save2[last2])
                print(count)
                count = count % (10 ** 9 + 7)
                last1 = i
                last2 = j
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        count += max(save1[len(nums1)-1] - save1[last1], save2[len(nums2)-1] - save2[last2])

        return count % (10 ** 9 + 7)


a = Solution()
print(a.maxSum(nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]))