class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        lens = len(cardPoints)
        remain = lens - k
        minnum = 0

        for i in range(remain):
            minnum = minnum + cardPoints[i]
        count = minnum
        num = minnum

        for i in range(remain,lens):
            count = count + cardPoints[i]
            num = num + cardPoints[i] - cardPoints[i - remain]
            minnum = min(minnum,num)

        return count - minnum
            
a = Solution()
print(a.maxScore([1,79,80,1,1,1,200,1],3))