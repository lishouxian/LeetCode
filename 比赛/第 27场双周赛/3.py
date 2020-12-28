

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        edges = [[] for i in range(n)]
        res = [set() for i in range(n)]
        
        for a,b in prerequisites:
            edges[a].append(b)
        visited = [0] * n

        def dfs(u: int):

            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
            for v in edges[u]:
                for ss in res[v]:
                    res[u].add(ss)
                res[u].add(v)

            # 将节点标记为「已完成」
            visited[u] = 2

        
        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(n):
            if not visited[i]:
                dfs(i)

        print(res)

        re = [False for i in range(len(queries))]
        for i in range(len(queries)):
            if queries[i][1] in res[queries[i][0]]:
                re[i] = True
        return re

mm = Solution()
print(mm.checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]))



