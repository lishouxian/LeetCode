class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        save = [0] * 10
        point = len(t) - 1
        for i in range(len(t) - 1, -1, -1):
            if save[int(t[i])] > 0:
                # if sum(save[int(t[i]) + 1:]) == 0:
                save[int(t[i])] -= 1
                # else:
                #     return False
            else:
                while s[point] != t[i]:
                    save[int(s[point])] += 1
                    point -=1
                    if point < 0: return False
                save[int(s[point])] += 1
                point -= 1
                if sum(save[int(t[i]) + 1:]) == 0:
                    save[int(t[i])] -= 1
                else:
                    return False

        for i in range(10):
            if save[i] != 0:
                return False

        return True


a = Solution()
print(a.isTransformable(s = "1", t = "2"))
