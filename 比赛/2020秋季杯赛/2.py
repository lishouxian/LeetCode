class Solution:
    def numWays(self, n: int, relation, k: int) -> int:
        rel = [[] for _ in range(n)]
        for rela in relation:
            rel[rela[0]].append(rela[1])
        num = [0 for i in range(n)]
        num2 = num
        i = 0
        for relations in rel[0]:
            num2[relations] += 1
        while i < k-1 :

            num = num2
            num2 = [0 for i in range(n)]
            for j in range(n):
                for relations in rel[j]:
                    num2[relations] += num [j]
            i = i +1

        return num2[-1]


a = Solution()
print(a.numWays(3,[[0,2],[2,1]],2))



