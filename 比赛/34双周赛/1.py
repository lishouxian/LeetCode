class Solution:
    def thousandSeparator(self, n: int) -> str:
        strnum = str(n)
        i = len(strnum) -1
        num = []
        while i >= 0:
            num.append(strnum[i])
            if (i + 2) % 3 == 0 and i != 0:
                num.append(".")
            i -= 1
        reversed(num)
        return "".join(num)

a = Solution()
print(a.thousandSeparator(1000))