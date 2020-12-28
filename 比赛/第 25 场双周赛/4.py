class Solution:
    def numberWays(self, hats) -> int:
        lens = len(hats)

        count = [0] * lens

        for i in range(lens):
            count[i] = len(hats[i])


        back = [1] * (lens + 1)
        back[lens-1] = count[lens -1 ]
        for i in range(lens-2,-1,-1):
            back[i] = count[i] * back[i+ 1]
        print(back)
        save = back[0]
        temp = hats[0]
        for i in range(1,lens):
            savenum = 0
            for j in temp:
                if j in hats[i]:
                    savenum += 1
            print(savenum , back[i+1])
            save -= savenum * back[i+1]
            temp = temp + hats[i]


            
        return  save
   
a = Solution()
print(a.numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))