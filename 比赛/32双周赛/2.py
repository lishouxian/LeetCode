class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        save = [1]
        for i in range(21):
            save.append(save[-1] * 2 + 1)
        #print(save)

        times = 0
        while k > 2:
            for i in range(len(save)-1,-1,-1):
                if k > save[i]:
                    if k - save[i] == 1: return (times+1) %2
                    k = save[i + 1] + 1 - k
                    times += 1
                    break

        if k == 1 : return (times)%2
        else: return (times +1)%2

a = Solution()
for i in range(1,15):
    print(a.findKthBit(n = 3, k = i))