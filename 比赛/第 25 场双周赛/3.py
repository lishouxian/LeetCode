class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        save = 0
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                if save == 0:
                    save = -1
                if save == 1:
                    return False
            if s1[i] > s2[i]:
                if save == 0:
                    save = 1
                if save == -1:
                    return False
        return True



a = Solution()
print(a.checkIfCanBreak('abe','acd'))



