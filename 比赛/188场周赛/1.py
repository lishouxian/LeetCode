class Solution:
    def buildArray(self, target,n):
        savenum = 1
        result = []
        for i in range(len(target)):
            while savenum != target[i]:
                result.append('Push')
                result.append('Pop')
                savenum += 1

            result.append('Push')
            savenum += 1

        return result

a = Solution()
print(a.buildArray([2,3,4],4))