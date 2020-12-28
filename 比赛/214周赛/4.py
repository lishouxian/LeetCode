class Solution:
    def kthSmallestPath(self, destination, k: int):
        def find(row, k, list):
            i = 0
            while (row + i) * (row + i - 1) // 2 <= k:
                i += 1

            list.append(i + row - 1)
            if k - (row + i - 2) * (row + i - 1) // 2 > 0:
                list = find(row - 1, k - (row + i - 2) * (row + i - 1) // 2, list)
            return list
        list = find(destination[0], k, [])
        print(list)


a = Solution()
print(a.kthSmallestPath(destination = [2,3], k = 3))
