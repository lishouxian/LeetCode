import copy

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        count = 0

        parent = [-1] * (n+1)
        rank = [0] * (n+1)

        def findroot(x):
            xtemp = x
            # print(xtemp, parent)
            while xtemp  < n and parent[xtemp] != -1:
                xtemp = parent[xtemp]

            # print(xtemp)
            return xtemp

        def union(x,y,count):
            if findroot(x) != findroot(y):
                if rank[findroot(x)] > rank[findroot(y)]:
                    parent[x] = y
                elif rank[findroot(x)] < rank[findroot(y)]:
                    parent[y] = x
                else:
                    parent[y] = x
                    rank[x] += 1
            else:
                count += 1

        for i in range(len(edges)):
            if edges[i][0] == 3:
                union(edges[i][1],edges[i][2],count)
        parenttemp = copy.deepcopy(parent)
        ranktemp = copy.deepcopy(rank)
        # print(parent)
        for i in range(len(edges)):
            if edges[i][0] == 1:
                union(edges[i][1],edges[i][2],count)
        parent = parenttemp
        rank = ranktemp

        for i in range(len(edges)):
            if edges[i][0] == 2:
                union(edges[i][1],edges[i][2],count)
        return count

a = Solution()

print(a.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
