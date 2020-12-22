class Solution:
    def largestNumber(self, cost, target):

        set = [False] * target
        import copy
        newcost = []
        for j in cost:
            if not j in newcost:
                newcost.append(j)

        newcost.sort()
        print(newcost)


        res = [False] * (target+1)
        res[0] = True



        for i in newcost:
            for j in range(target, -1,-1):
                if res[j % i]:res[j] == True


            



        print(yushu)






   
a = Solution()
print(a.largestNumber([7,6,5,5,5,6,8,7,8],12))