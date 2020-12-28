class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        res = [True for i in range(2 ** k)]
        print(res)
        for i in range(len(s)-k+1):
            string1 = s[i:i+k]
            print(int(string1,2))
            res[int(string1,2)] = False
        print(res)
        for i in range(2 ** k):
            if res[i]:return False
        print(res)
        return True
            





a = Solution()
print(a.hasAllCodes(s = "00110", k = 2))