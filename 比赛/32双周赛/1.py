import copy


class Solution:
    def makeGood(self, s: str) -> str:
        for j in range(100):
            scopy = copy.deepcopy(s)
            for i in range(len(s)-1):
                if abs(ord(s[i]) -ord(s[i+1])) == 32:
                    scopy = s[:i] + s[i+2:]
            s = scopy
        return s

a = Solution()
print(a.makeGood("l"))