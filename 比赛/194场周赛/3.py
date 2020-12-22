class Solution:
    def avoidFlood(self, rains):
        res = [0 for _ in range(len(rains))]
        nums = 0
        used = 0
        numshelp = []
        save = zip(rains,res)
        save1 = dict(save)
        save2 = dict(save)
        save = dict(save)
        for i in range(len(rains)):
            if rains[i] == 0:nums += 1
            elif save.get(rains[i], 0) == 0:
                save[rains[i]] = 1
                res[i] = -1
                save1[rains[i]] = nums
                save2[rains[i]] = i
            elif save.get(rains[i], 0) == 1:
                if nums == save1[rains[i]] or nums == used: return []
                else:
                    
                    save1[rains[i]] = nums
                    used += 1
                    numshelp.append([save2[rains[i]],rains[i]])
                    res[i] = -1
        j = 0 
        #print(numshelp)
        for i in range(len(numshelp)):
            j = numshelp[i][0]
            while res[j] != 0 and j < len(res):
                j += 1
            res[j] = numshelp[i][1]
        j = 0 
        while j < len(res):
            if res[j] == 0: res[j] = 1
            j += 1
        return res


a = Solution()
print(a.avoidFlood([2,3,0,0,3,1,0,1,0,2,2]))