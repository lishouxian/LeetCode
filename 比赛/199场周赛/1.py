class Solution:
    def getStrongest(self, arr, k):
        arr.sort()
        nummid = arr[(len(arr) - 1)//2]

        left = 0
        right = len(arr)-1
        res = []
        p = 1
        while p <= k:
            if arr[right] - nummid >= nummid - arr[left]:
                res.append(arr[right])
                p += 1
                right -= 1
                continue
            else:
                res.append(arr[left])
                p += 1
                left += 1
        return res



a = Solution()
print(a.getStrongest(arr = [6,7,11,7,6,8], k = 5))