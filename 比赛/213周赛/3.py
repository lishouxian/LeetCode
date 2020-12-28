import heapq
class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        help = []
        i = 1
        res = 0
        while len(help) < ladders and i < len(heights):
            if heights[i] > heights[i-1]:
                help.append(heights[i] - heights[i-1])
            res = i
            i += 1


        heapq.heapify(help)
        count = 0

        while i < len(heights):

            if heights[i] > heights[i-1]:
                if ladders == 0 or heights[i] - heights[i-1] <= help[0]:
                    count += heights[i] - heights[i-1]
                else:
                    count += help[0]
                    heapq.heappushpop(help, heights[i] - heights[i-1])
            if count <= bricks:
                res = i

            i += 1

        return res





a = Solution()
print(a.furthestBuilding([17,16,5,10,10,14,7],
74,
6))




