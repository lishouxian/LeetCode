class Solution:
    def unhappyFriends(self, n: int, preferences, pairs):
        def getpair(x):
            for k in range(len(pairs)):
                if x in pairs[k]:
                    return sum(pairs[k]) - x

            return 0

        res = [0] * n
        for i in range(n - 1):
            for j in range(i + 1, n):
                p, q = preferences[i], preferences[j]
                if p.index(j) < p.index(getpair(i)) and q.index(i) < q.index(getpair(j)):
                    res[i] = 1
                    res[j] = 1

        return sum(res)


a = Solution()
print(a.unhappyFriends(n = 2, preferences = [[1], [0]], pairs = [[1, 0]]))