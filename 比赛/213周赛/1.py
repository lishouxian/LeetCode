class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        i = 0
        while i < len(arr):
            j = 0
            for j in range(len(pieces)):
                if pieces[j][0] == arr[i]:
                    for k in range(len(pieces[j])):
                        if pieces[j][k] == arr[i]:
                            i += 1
                        else:
                            return False
                    break
            else:
                return False
        return True

a = Solution()
print(a.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))