class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int):
        def getlength(m):
            save = [0]
            for i in range(1,len(m)):
                if s[i] != s[i-1]:
                    save.append(i)
            save.append(len(m))
            newsave = [save[i] - save [i-1] for i in range(1,len(save))]
            count1 = 0
            for j in newsave:
                if j == 1:count1 +=1

            return len("".join(newsave))+ len(newsave)


        res = 1000
        for i in range(len(s)):
            res = min(res,getlength(s[:i] + s[i+1:]))

        return res

a = Solution()
print(a.getLengthOfOptimalCompression(s = "aaabcccd", k = 2))