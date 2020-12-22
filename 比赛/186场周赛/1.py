class Solution:
    def maxScore(self, s: str) -> int:
        right = 0
        left = 0
        for i in range(1,len(s)):
            if s[i] == '1': right += 1

        if s[0] == '0': left += 1

        maxnum = right + left

        for i in range(1,len(s)-1):
            if s[i] == '1': 
                right -= 1
            else: 
                left += 1
            maxnum = max(maxnum,left + right)
        return maxnum






a = Solution()
print(a.maxScore("0"))