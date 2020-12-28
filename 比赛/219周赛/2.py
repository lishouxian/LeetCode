import heapq


class Solution:
    def eatenApples(self, apples, days):
        for i in range(len(days)):
            days[i] += i
        lst = []
        m = {}
        count = 0
        for i in range(len(apples)):
            heapq.heappush(lst,days[i])
            if days[i] in m:
                m[days[i]] += apples[i]
            else:
                m[days[i]] = apples[i]

            while lst and (lst[0] <= i  or m[lst[0]] == 0) :
                heapq.heappop(lst)
            if lst:
                m[lst[0]] -= 1
                count += 1

        i = len(apples)

        while lst:
            while lst and (lst[0] <= i  or m[lst[0]] == 0) :
                heapq.heappop(lst)
            if lst:
                m[lst[0]] -= 1
                count += 1

            i += 1
        return count

a = Solution()
print(a.eatenApples([3,0,0,0,0,2], days = [3,0,0,0,0,2]))
















