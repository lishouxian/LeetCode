class Solution:
    def minInsertions(self, s: str) -> int:
        len1 = len(s)
        print(s)
        s = list(s)
        i = 0

        while i < len(s):
            if s[i]==')':
                if i+1 <len(s) and s[i+1]==')':
                    i += 1
                else:
                    s[i] = '))'
            i += 1
        s = ''.join(s)
        print(s)
        i = j = len(s) - 1
        count = 0
        numofleft = 0
        while i > -1:
            if s[i] == '(':
                numofleft += 1
                smallcount = 2
                while j > i and smallcount > 0:
                    if s[j] == ')':
                        smallcount -= 1
                        j -= 1
                    else:
                        j -= 1
                count += smallcount
            i -= 1
        numofright = count + len(s) - numofleft
        print(count)
        if numofright% 2 == 1:
            numofright += 1

        return int(numofright * 1.5 - len1)

a = Solution()
print(a.minInsertions(s = "("))