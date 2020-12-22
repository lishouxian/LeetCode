class Solution:
    def maxDiff(self, num: int) -> int:
        strnum = str(num)
        count = 0
        lens = len(strnum)
        save = -1

        if strnum[0] == '1':
            for i in range(1,lens):
                if save == -1:
                    if strnum[i] != '0' and strnum[i] != '1':
                        count += 10 ** (lens - i-1) * (int(strnum[i]) - 0)
                        save = strnum[i]
                else:
                    if strnum[i] == save:
                        count += 10 ** (lens - i-1) * (int(strnum[i]) - 0)
        else:
            save = strnum[0]
            count += 10 ** (lens - 0-1) * (int(strnum[0]) - 1)
            for i in range(1,lens):
                if strnum[i] == save:
                    count += 10 ** (lens - i-1) * (int(strnum[i]) - 1)

        save = -1

        for i in range(lens):
            if save == -1:
                if strnum[i] != '9':
                    count += 10 ** (lens - i-1) * (9 - int(strnum[i]))
                    save = strnum[i]
            else:
                if strnum[i] == save:
                    count += 10 ** (lens - i-1) * (9 - int(strnum[i]))

        return count


a = Solution()
print(a.maxDiff(1101057))