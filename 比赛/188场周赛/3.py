class Solution:
    def minTime(self, n: int, edges, hasApple):
        
        tree = [[] for i in range(n)]
        tree2 = [0] * n
        for i in edges:
            tree[i[0]].append(i[1])
        for i in edges:
            tree2[i[1]]=i[0]

        count = -2

        def backtrack(node):
            for i in tree[node]:
                backtrack(i)
            if hasApple[node] == True:

                hasApple[tree2[node]] = True
            
        backtrack(0)

        for i in hasApple:
            if i: count += 2


        return max(0,count)



a = Solution()
print(a.minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]))