class Solution:
    def minJump(self, jump):

        jumpnew = [jump[i] + i for i in range(len(jump))]
        print(jumpnew)
        right = 0
        m = 0
        while right < len(jump):
            #print(right)
            if right > len(jump)-1:
                break
            if jumpnew[right] > len(jump)-1:
                m = m + 1
                break
            if jumpnew[jumpnew[right]] < max(jumpnew[right:jumpnew[right]+1]) or jumpnew[max(jumpnew[right:jumpnew[right]+1])] > len(jump)-1:
                right = max(jumpnew[right:jumpnew[right] + 1])
                #right = jumpnew[jumpnew[jumpnew[right]]]
            elif jumpnew[max(jumpnew[right:jumpnew[right]+1])]:
                right = jumpnew[jumpnew[right]]
            m = m + 2
        return m



a = Solution()
print(a.minJump([2,4,1,1,1]))