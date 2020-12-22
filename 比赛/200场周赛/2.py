class Solution:
    def getWinner(self, arr, k: int) -> int:
        if k >= len(arr) - 1: return max(arr)
        count = 0
        i = 0
        j = 1
        while count < k:
            if j > len(arr) - 1:break
            if arr[i] > arr[j]:
                count += 1
            else:
                i = j
                count = 1
            j += 1
        return arr[i]

a = Solution()
print(a.getWinner(arr = [2,1,3,5,4,6,7], k = 2))