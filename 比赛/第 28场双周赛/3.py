class Solution:
    def minSumOfLengths(self, arr, target) -> int:
        save = []
        left = 0
        count = 0
        i = 0 
        while i < len(arr)+1:
            if count < target:
                if i == len(arr):break
                count += arr[i]
                i += 1
            elif count == target:
                save.append([left,i])
                count -= arr[left]
                left += 1
            else:
                count -= arr[left]
                left += 1
        
        if len(save) <= 1:return -1
        dp = [-1 for i in range(10000000)]
        minnum = save[0][1] - save[0][0]
        dp[save[0][1]] = minnum
        res = -1
        #print(save)
        for i,j in save[1:]:
            
            for k in range(j,-1,-1):
                if dp[k]> 0: break
                dp[k] = minnum
            dp[j] = min(minnum,j-i)
            minnum = dp[j]

            #print(dp[j])
            
            if dp[i] > 0:
                help = dp[i]
                if res == -1: res = help + j-i
                else: res = min(res,help + j-i)
                
        return res


mm = Solution()
print(mm.minSumOfLengths(arr = [3,2,2,4,3], target = 3))



