class Solution:
    def destCity(self, paths):
        start = []
        for path in paths:
            start.append(path[0])
        for path in paths:
            if not path[1] in start:
                return path[1]





a = Solution()
print(a.destCity([["B","C"],["D","B"],["C","A"]]))