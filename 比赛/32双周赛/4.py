class Solution:
    def longestAwesome(self, s: str):
        change = [2 ** i  for i in range(10)]
        #print(change)
        help = [0] * len(s)
        for i in range(len(s)):
            help[i] = help[i-1] ^ change[int(s[i])]
        help.insert(0,0)
        print(help)
        maxnum = 0
        if len(help) > 90000:
            for i in range(len(help)):
                savemax = maxnum
                for j in range(i + savemax + 1, len(help)):
                    if help[i] ^ help[j] < 2 or help[i] ^ help[j] in change:
                        print(i, j)
                        maxnum = max(maxnum, j - i)
                    else:
                        return maxnum
        for i in range(len(help)):
            savemax = maxnum
            for j in range(i + savemax + 1,len(help)):
                if  help[i] ^ help[j] < 2 or help[i] ^ help[j] in change:
                    print(i,j)
                    maxnum = max(maxnum,j-i)
        return maxnum


a = Solution()
print(a.longestAwesome("940884"))