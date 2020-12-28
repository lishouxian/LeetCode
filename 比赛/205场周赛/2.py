class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        save1 = []
        save2 = []
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                save1.append(nums1[i] * nums1[j])
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                save2.append(nums2[i] * nums2[j])

        save1.sort()
        save2.sort()
        nums1.sort()
        nums2.sort()

        count = 0
        i = j = 0
        while i < len(nums1) and j < len(save2):
            if nums1[i] * nums1[i] == save2[j]:
                save = nums1[i] * nums1[i]
                m = n = 0
                while i < len(nums1) and nums1[i] * nums1[i] == save:
                    i += 1
                    m += 1
                while j < len(save2) and save2[j] == save:
                    j += 1
                    n += 1
                count += m * n
            elif nums1[i] * nums1[i] > save2[j]:
                j += 1
            else:
                i += 1
        i = j = 0

        while i < len(nums2) and j < len(save1):
            if nums2[i] * nums2[i] == save1[j]:
                save = nums2[i] * nums2[i]
                m = n = 0
                while i < len(nums2) and nums2[i] * nums2[i] == save:
                    i += 1
                    m += 1
                while j < len(save1) and save1[j] == save:
                    j += 1
                    n += 1
                count += m * n
            elif nums2[i] * nums2[i] > save1[j]:
                j += 1
            else:
                i += 1

        return count


a = Solution()

print(a.numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]))