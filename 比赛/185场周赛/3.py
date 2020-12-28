class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        m =[0,0,0,0,0]
        save = 0
        for croak in croakOfFrogs:
            if croak == 'c':
                if m[4] > 0:
                    save = max(m[4], save)
                    for i in range(len(m)):
                        m[i] -= m[4]
                m[0] += 1
            if croak == 'r':
                m[1] += 1
            if croak == 'o':
                m[2] += 1
            if croak == 'a':
                m[3] += 1
            if croak == 'k':
                m[4] += 1
            if not m[0] >= m[1] >= m[2] >= m[3] >= m[4]:
                return(-1)

        if m[-1] ==m[0]:
            return max(m[4], save)
        else:return -1



a = Solution()
print(a.minNumberOfFrogs('croakcrook'))