class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = [0]
        save = []

        def backtrack(count, i):
            if i == len(s):
                res[0] = max(res[0], count)
            else:
                for j in range(i + 1, len(s)+1):
                    if s[i:j] not in save:
                        save.append(s[i:j])
                        backtrack(count + 1, j)
                        save.remove(s[i:j])

        backtrack(0, 0)
        return res[0]


a = Solution()
print(a.maxUniqueSplit("aaa"))
