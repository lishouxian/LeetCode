class Solution:
    def countTriplets(self, arr):
        save = 0
        newlist =[0]
        count = 0
        for i in arr:
            save = i^save
            newlist.append(save)
        print(newlist)
        for i in range(len(newlist)):
            for j in range(i+1,len(newlist)):
                save = newlist[j] ^ newlist[i]
                for k in range(j+ 1, len(newlist)):
                    if save == newlist[j] ^ newlist[k]:
                        count +=1
        return count





a = Solution()
print(a.countTriplets([1,3,5,7,9]))
