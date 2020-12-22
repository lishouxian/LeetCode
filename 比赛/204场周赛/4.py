class Solution:
    def containsPattern(self, arr, m: int, k: int):
        total = m * k
        for i in range(len(arr) - total +1):
            save = arr[i:i+m]
            for j in range(0,total,m):
                if save != arr[i+j:i+j+m]:
                    break
            else: return True
        return False




a = Solution()
print(a.containsPattern(arr = [2,2], m = 1, k = 2))