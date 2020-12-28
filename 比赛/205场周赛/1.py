class Solution:
    def modifyString(self, s: str) -> str:
        result = list(s)
        result.append("a")
        for i in range(len(s)):
            if s[i] == '?':
                if result[i-1] != 'b' and result[i+1] != 'b':
                    result[i] = 'b'
                elif result[i - 1] != 'a' and result[i + 1] != 'a':
                    result[i] = 'a'
                elif result[i - 1] != 'c' and result[i + 1] != 'c':
                    result[i] = 'c'

        return "".join(result[:-1])