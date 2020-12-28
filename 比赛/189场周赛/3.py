class Solution:
    def peopleIndexes(self, favoriteCompanies):
        res = [i for i in range(len(favoriteCompanies))]
        #print(res)
        for i in range(len(favoriteCompanies)):
            for j in range(i,len(favoriteCompanies)):
                if len(favoriteCompanies[i]) == len(favoriteCompanies[j]):
                    pass
                elif len(favoriteCompanies[i]) > len(favoriteCompanies[j]):
                    for m in favoriteCompanies[j]:
                        if not m in favoriteCompanies[i]:
                            break
                    else:
                        if j in res:
                            res.remove(j)
                else:
                    for m in favoriteCompanies[i]:
                        if not m in favoriteCompanies[j]:
                            break
                    else:
                        if i in res:
                            res.remove(i)




        return res


a = Solution()
print(a.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))